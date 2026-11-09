# Flask hostname and counter app

This small Flask app greets visitors with the machine's hostname at `/` and
increments a counter at `/counter`.

The counter is deliberately stored in a module-level global. It is only
process-local: it resets when the process restarts, and separate workers or
instances keep separate counters. This intentionally demonstrates why
application state should not be stored in a web process's memory.

Install dependencies and run locally with:

```sh
pip install -r requirements.txt
flask --app app run
```

The `Procfile` starts the app with Gunicorn on platforms that support Procfiles.
