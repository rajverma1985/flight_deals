from dotenv import load_dotenv

load_dotenv()


if __name__ == "__main__":
    from app.main.main import run_app
    run_app()
