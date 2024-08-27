import pytest
import subprocess


@pytest.fixture(scope="session", autouse=True)
def start_webserver():
    server = subprocess.Popen(["python", "-m", "http.server", "8000"], cwd="fixtures")
    yield
    server.terminate()
    server.wait()
