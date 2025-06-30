import gradio as gr
from gym_trainer.crew import GymTrainer
import warnings

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run_crew(user_name, user_email, user_lifestyle, user_profile, user_goal):
    try:
        inputs = {
            'user_name': user_name,
            'user_email': user_email,
            'user_lifestyle': user_lifestyle,
            'user_profile': user_profile,
            'user_goal': user_goal
        }
        GymTrainer().crew().kickoff(inputs=inputs)
        return f"✅ Crew executed successfully. Email sent to {user_email}!"
    except Exception as e:
        return f"❌ An error occurred while running the crew: {str(e)}"

with gr.Blocks(title="AI Gym Trainer") as demo:
    gr.Markdown("## 🏋️ AI-Powered Gym Trainer\nFill in your details to receive a custom fitness plan via email.")

    with gr.Row():
        user_name = gr.Textbox(label="Your Name", placeholder="e.g. Harjas")
        user_email = gr.Textbox(label="Your Email", placeholder="e.g. example@gmail.com")

    with gr.Row():
        user_lifestyle = gr.Textbox(label="Lifestyle Description", placeholder="e.g. I have a sitting job and minimal body movement.")
        user_profile = gr.Textbox(label="Your Profile", placeholder="e.g. I am 180cm tall and weigh 90kg.")

    user_goal = gr.Textbox(label="Your Goal", placeholder="e.g. Lose 5kg of weight")

    submit_btn = gr.Button("Get My Plan 🚀")
    output = gr.Textbox(label="Status", lines=2)

    submit_btn.click(
        fn=run_crew,
        inputs=[user_name, user_email, user_lifestyle, user_profile, user_goal],
        outputs=output
    )

if __name__ == "__main__":
    demo.launch()
