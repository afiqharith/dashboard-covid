from assets import Dashboard
import datetime
import os

app = Dashboard().start_server

if __name__ == "__main__":
    try:
        app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    except KeyboardInterrupt:
        print(f"Server shutting down on {datetime.datetime.now}")
