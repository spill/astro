import nextcord
from nextcord.ext import commands
from canvasapi import Canvas
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('canvas_config.env')

API_URL = 'https://csufullerton.instructure.com/'
API_KEY = os.getenv('CANVAS_API_KEY')

canvas = Canvas(API_URL, API_KEY)

# Mapping of course identifiers to Canvas course IDs
COURSE_IDS = {
    "Biology": "3418432",
    "BiologyL": "3418484",
    "CPSC 223P": "3426940",
    "CPSC 253": "3434633",
    "Calculus": "3423370",
    "170A": "3449504"
}

class Canvas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def check(self, ctx, course_identifier: str):
        course_id = COURSE_IDS.get(course_identifier)
        if not course_id:
            await ctx.send(f"No course found with identifier {course_identifier}.")
            return

        course = canvas.get_course(course_id)
        assignments = course.get_assignments()
        response = f"Assignments for {course.name}:\n"
        for assignment in assignments:
            due_date = assignment.due_at or "No due date"
            response += f"- {assignment.name} (Due {due_date})\n"

            if len(response) > 2000:
                await ctx.send(response[:2000])
                response = response[2000:]

        if response:  # Send any remaining text
            await ctx.send(response)

    @commands.command()
    async def list(self, ctx):
        response = "Available courses:\n"
        for identifier, course_id in COURSE_IDS.items():
            course = canvas.get_course(course_id)
            response += f"{identifier} - {course.name}\n"

            if len(response) > 1900:
                await ctx.send(response)
                response = ""

        if response:  # Send any remaining text
            await ctx.send(response)

def setup(bot):
    bot.add_cog(Canvas(bot))
