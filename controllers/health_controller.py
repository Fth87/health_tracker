import views
import services

def main():
    views.display_welcome_message()
    user_data = views.get_user_data()
    summary = services.get_health_summary(user_data)
    aiData = services.ai_data(user_data)
    views.display_summary(summary)
    views.display_summary(aiData)

if __name__ == "__main__":
    main()
