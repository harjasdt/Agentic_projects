from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import smtplib
from email.message import EmailMessage
import os


class EmailToolInput(BaseModel):
    """Input schema for EmailTool."""
    user_email: str = Field(description="email id of the user")
    fitness_plan_summary: str = Field(description="email body that contains the summary of the fitness plan ")
    email_subject:str = Field(description="motivational subject for the email")
    

class EmailTool(BaseTool):
    name: str = "email_notifier_tool"
    description: str = (
        "This sends an email notification to the user about their workout plan"
    )
    args_schema: Type[BaseModel] = EmailToolInput

    def _run(self, user_email: str,fitness_plan_summary: str,email_subject:str) -> str:
        # print(user_email,fitness_plan_summary)
        try:

            # Create email
            msg = EmailMessage()
            msg["Subject"] = email_subject
            msg["From"] = os.getenv("SMTP_SENDER_EMAIL")  # e.g. 'your_email@example.com'
            msg["To"] = user_email
            msg.set_content(fitness_plan_summary,subtype="html")

            # SMTP credentials from environment
            smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
            smtp_port = int(os.getenv("SMTP_PORT", 587))
            smtp_user = os.getenv("SMTP_SENDER_EMAIL")
            smtp_pass = os.getenv("SMTP_PASSWORD")

            # Send the email
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_user, smtp_pass)
                server.send_message(msg)

            return f"Email successfully sent to {user_email}"

        except Exception as e:
            return f"Failed to send email: {str(e)}"
