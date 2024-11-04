import flet as ft
import speedtest
from time import sleep

def main(page: ft.Page):
    page.title = "Internet Speedtest app"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    padding = 40
    page.fonts = {
        "Cream Beige": "fonts/Cream Beige.otf",
        "Energy Station": "fonts/Energy Station.otf",
        "Shine Bubble Decoration - (Demo) hanscostudio.com": "fonts/Shine Bubble Decoration - (Demo) hanscostudio.com.ttf",
        "Summer Morning": "fonts/Summer Morning.otf"
    }

    # Initialize speedtest
    st = speedtest.Speedtest()

    # Defining the app title
    internet = ft.Text(value="Internet", font_family="Cream Beige", size=45, color="red")
    speed_test = ft.Text(value="Speedtest", font_family="Cream Beige", size=45, color="red")
    app_title = ft.Row(
        controls=[internet, speed_test],
        alignment="center"
    )

    # Defining the lines in the container
    line_1 = ft.Text(value=">> Please Wait... ", font_family="Summer Morning", size=13, color="white")
    line_2 = ft.Text(value="", size=13, font_family="Summer Morning", color="white")
    progressText1 = ft.Text(value=" ", font_family="Summer Morning", size=13, color="white")
    line_3 = ft.Text(value=" ", size=13, font_family="Summer Morning", color="white")
    progress_bar1 = ft.ProgressBar(width=400, bgcolor="white", color="red", opacity=0)
    progressText2 = ft.Text(value=" ", font_family="Summer Morning", size=13, color="white")
    progressRow1 = ft.Row([progressText1, progress_bar1], opacity=0)
    progress_bar2 = ft.ProgressBar(width=400, bgcolor="white", color="red", opacity=0)
    progressRow2 = ft.Row([progressText2, progress_bar2], opacity=0)
    download_speed_box = ft.TextField(hint_text=" ", color="white", border_color="white", width = 120)
    upload_speed_box = ft.TextField(hint_text=" ", color="white", border_color="white", width = 120)
    line_4 = ft.Text(value=" ", font_family="Summer Morning", size=13, color="white")
    row4 = ft.Row([line_4, download_speed_box], opacity = 0)
    line_5 = ft.Text(value=" ", font_family="Summer Morning", size=13, color="white")
    line_6 = ft.Text(value=" ", font_family="Summer Morning", size=13, color="white")
    line_7 = ft.Text(value="Calculating... ", font_family="Summer Morning", size=13, color="white")
    row7 = ft.Row([line_7, upload_speed_box], opacity = 0)
    line_8 = ft.Text(value=" ", font_family="Summer Morning", size=13, color="white")
    line_9 = ft.Text(value=" ", font_family="Summer Morning", size=13, color="white")

    terminalwords = ft.Column([line_1, line_2, line_3, progressRow1, row4, line_5, line_6, progressRow2, row7, line_8, line_9])

    # Defining the container
    get_container = ft.Container(
        content=terminalwords,
        width=200,
        height=100,
        bgcolor="blue",
        border_radius=45,
        padding=30,
        animate_size=ft.animation.Animation(1000, "bounceOut")
    )

    # SpeedTest function
    def SpeedTest(e):
        progressRow2.opacity = 0
        progressRow1.opacity = 0
        progress_bar1.value = None
        progress_bar1.value = None
        row4.opacity = 0
        row7.opacity = 0
        line_1.value = " "
        line_2.value = " "
        line_3.value = " "
        line_4.value = " "
        line_5.value = " "
        line_6.value = " "
        line_7.value = " "
        line_8.value = " "
        download_speed_box.value = ""
        upload_speed_box.value = " "
        get_container.update()
        get_container.width = 700
        get_container.height = 450
        get_container.update()
        line_1.value = ">> Calculating download speed, Please wait..."
        get_container.update()
        sleep(2)

        # Declaring server and inserting line 2
        ideal_server = st.get_best_server()
        city = ideal_server["name"]
        country = ideal_server["country"]
        cc = ideal_server["cc"]
        line_2.value = f">> Finding the best possible servers in {city}, {country}, {cc}"
        get_container.update()
        sleep(2)

        # Calculate download speed
        line_3.value = ">> Connection established, fetching download speed..."
        progressRow1.opacity = 1
        progress_bar1.opacity = 1
        get_container.update()
        sleep(3)

        # Update download speed
        download_speed = st.download() / (1024 * 1024)  # in Mbps
        row4.opacity = 1
        line_4.value = ">> The download speed is "
        download_speed_box.value = f"{round(download_speed, 2)} Mbps"
        progress_bar1.value = 1
        get_container.update()

        # Calculating upload speed
        line_5.value = ">> Calculating upload speed, Please wait..."
        get_container.update()

        line_6.value = ">> Fetching upload speed..."
        progressRow2.opacity = 1
        progress_bar2.opacity = 1
        get_container.update()
        sleep(2)

        # Update upload speed
        upload_speed = st.upload() / (1024 * 1024)  # in Mbps
        row7.opacity = 1
        line_7.value = ">> The upload speed is "
        upload_speed_box.value = f"{round(upload_speed, 2)} Mbps"
        progress_bar2.value = 1
        get_container.update()

        # Completion message
        line_8.value = ">> Task completed successfully!"
        line_9.value = "App designed by Adetoro Andrew"
        get_container.update()

    play_btn = ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, icon_color="red", icon_size=50, on_click=SpeedTest)

    page.add(
        app_title,
        get_container,
        play_btn
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER, assets_dir="assets")
