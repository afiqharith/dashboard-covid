from assets import Dashboard
import datetime

app = Dashboard().start_server

if __name__ == "__main__":
    try:
        app.run(debug = True)
    except KeyboardInterrupt:
        print(f"Server shutting down on {datetime.datetime.now}")
