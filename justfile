# Notify today birthdays
today:
    uv run python main.py --today

# Notify next birthdays
next:
    uv run python main.py --next

# Sync uv
[macos]
sync:
    uv sync --no-group prod

# Sync uv
[linux]
sync:
    uv sync --no-dev --group prod

# Deploy program
deploy:
    git pull
    just sync
