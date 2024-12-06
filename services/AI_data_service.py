import utils
import views
import threading


def ai_data(data):
    loading_thread = threading.Thread(target=views.loading_indicator)
    loading_thread.daemon = True
    loading_thread.start()

    health_insights = utils.get_gemini_data(data)

    loading_thread.do_run = False
    print("\rSelesai!")
    return {"Hasil analisis oleh AI \n": health_insights}