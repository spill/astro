import nextcord
from nextcord.ext import commands
from canvasapi import Canvas
import os
from dotenv import load_dotenv

# Load environment variables from config.env
load_dotenv('canvas_config.env')

API_URL = 'https://csufullerton.instructure.com/'
API_KEY = os.getenv('CANVAS_API_KEY')  # Fetch API key from environment variable
COURSE_ID = '3418432'  # Replace with your actual course ID

canvas = Canvas(API_URL, API_KEY)
course = canvas.get_course(COURSE_ID)

class Canvas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.course = course

    @commands.command()
    async def check_canvas(self, ctx):
        assignments = self.course.get_assignments()
        if assignments:
            response = "Upcoming Assignments:\n"
            for assignment in assignments:
                due_date = assignment.due_at or "No due date"
                assignment_info = f"{assignment.name} - is due on {due_date}\n"
                # Check if adding the next assignment would exceed the limit
                if len(response) + len(assignment_info) > 2000:
                    await ctx.send(response)  # Send the current response
                    response = ""  # Reset the response for the next set of assignments
                response += assignment_info
        else:
            response = "No new assignments found."
        
        # Send any remaining response text
        if response:
            await ctx.send(response)

def setup(bot):
    bot.add_cog(Canvas(bot))