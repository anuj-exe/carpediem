import openai
from datetime import datetime
import random

# Set up OpenAI GPT API (replace with your own key)
openai.api_key = ''

# Updated user profiles
users = [
    {
        "name": "Alice",
        "age": 29,
        "job": "Software Developer",
        "challenges": ["waking up early", "too much screen time"],
        "personality": "creative and introverted."
    },
    {
        "name": "Bob",
        "age": 42,
        "job": "Teacher",
        "challenges": ["going to bed on time", "stress management"],
        "personality": "empathetic and hardworking."
    },
    {
        "name": "Charlie",
        "age": 35,
        "job": "Graphic Designer",
        "challenges": ["procrastination", "fitness consistency"],
        "personality": "artistic and energetic."
    },
    {
        "name": "Dana",
        "age": 24,
        "job": "Retail Store Cashier",
        "challenges": ["overworked", "study-life balance", "sleep deprivation"],
        "personality": "resilient and determined."
    },
    {
        "name": "Michael",
        "age": 22,
        "job": "College Student",
        "challenges": ["Balancing studies and part-time job", "Distraction from social media"],
        "personality": ["Energetic", "Social", "Loves new experiences"]
    },
    {
        "name": "Laura",
        "age": 45,
        "job": "Project Manager",
        "challenges": ["Work-life balance", "Feeling burned out"],
        "personality": ["Organized", "Ambitious", "Struggles with self-care"]
    },
    {
        "name": "David",
        "age": 29,
        "job": "Chef",
        "challenges": ["Irregular hours", "Unhealthy eating habits"],
        "personality": ["Passionate about food", "Creative", "Can be impulsive"]
    },
    {
        "name": "Anna",
        "age": 34,
        "job": "Software Engineer",
        "challenges": ["Perfectionism", "Struggles with public speaking"],
        "personality": ["Analytical", "Introverted", "Loves problem-solving"]
    },
    {
        "name": "Tom",
        "age": 50,
        "job": "Sales Executive",
        "challenges": ["Stress from targets", "Poor work-life balance"],
        "personality": ["Charismatic", "Persuasive", "Sometimes feels under pressure"]
    },
    {
        "name": "Chloe",
        "age": 27,
        "job": "Yoga Instructor",
        "challenges": ["Self-doubt", "Pressure to maintain a perfect lifestyle"],
        "personality": ["Peaceful", "Health-conscious", "Sometimes overly critical"]
    },
    {
        "name": "Brian",
        "age": 40,
        "job": "Financial Analyst",
        "challenges": ["Anxiety about job stability", "Balancing family time"],
        "personality": ["Detail-oriented", "Practical", "Sometimes cynical"]
    },
    {
        "name": "Jess",
        "age": 23,
        "job": "Graphic Designer",
        "challenges": ["Creative blocks", "Overthinking ideas"],
        "personality": ["Imaginative", "Playful", "Can be disorganized"]
    }
]

#get time of day
def get_time_of_day():
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return "morning"
    elif 12 <= current_hour < 17:
        return "afternoon"
    elif 17 <= current_hour < 21:
        return "evening"
    else:
        return "night"

# Function to use GPT to generate a concise, specific task suggestion
def generate_task_suggestion(user):
    time_of_day = get_time_of_day()
    
    prompt = f"""
    You are an assistant helping users build good habits. For the user:
    
    Name: {user['name']}
    
    Suggest one concise, specific mini task for them to do in the {time_of_day}. Use minimal words and address them directly.
    """
    
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=30  # Limit response length to reduce cost
    )
    
    task_suggestion = response.choices[0].text.strip()
    return task_suggestion

# Function to randomly select a user and generate a task for them
def assign_task_to_user():
    user = random.choice(users)
    task = generate_task_suggestion(user)
    
    return f"{task}"

# Assign a task to a random user and print it
if __name__ == "__main__":
    print(assign_task_to_user())
