
"""
Demo script for the Electrical and Computer Engineering Program Chatbot
This script demonstrates various interactions with the chatbot
"""

from chatbot import StudentChatbot

def run_demo():
    """Run a demonstration of the chatbot functionality"""
    chatbot = StudentChatbot()
    
    print("=" * 80)
    print(" ELECTRICAL AND COMPUTER ENGINEERING PROGRAM CHATBOT DEMO")
    print("=" * 80)
    
    
    demo_questions = [
        "برنامج",  
        "program",  
        "ساعات",  
        "credits", 
        "ECE-C101",
        "مقررات", 
        "courses",
        "درجات",  
        "grades",  
        "تسجيل",   
        "registration",
        "مرشد",    
        "advisor", 
        "help",     
        "exit"      
    ]
    
    for i, question in enumerate(demo_questions, 1):
        print(f"\n{'='*60}")
        print(f"Demo {i}: '{question}'")
        print(f"{'='*60}")
        
        response = chatbot.get_response(question)
        print(f" Response: {response}")
        
        
        import time
        time.sleep(1)
    
    print(f"\n{'='*80}")
    print(" Demo completed! The chatbot is ready to use.")
    print("Run 'python chatbot.py' to start an interactive session.")
    print(f"{'='*80}")

if __name__ == "__main__":
    run_demo() 