import pytest
import allure
import os
import shutil
from pathlib import Path

# ==============================
# GLOBAL PATHS
# ==============================
ARTIFACTS_DIR = Path("artifacts")
SCREENSHOTS_DIR = ARTIFACTS_DIR / "screenshots"
VIDEOS_DIR = ARTIFACTS_DIR / "videos"


# ==============================
# SESSION SETUP / CLEANUP
# ==============================
@pytest.fixture(scope="session", autouse=True)
def prepare_artifacts_dir():
    """
    Clean artifacts directory before test session starts
    """
    if ARTIFACTS_DIR.exists():
        shutil.rmtree(ARTIFACTS_DIR)

    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    VIDEOS_DIR.mkdir(parents=True, exist_ok=True)


# ==============================
# BROWSER CONTEXT
# ==============================
@pytest.fixture(scope="function")
def context(browser):
    """
    New isolated browser context per test
    Video is recorded but may be deleted later
    """
    context = browser.new_context(
        record_video_dir=str(VIDEOS_DIR),
        record_video_size={"width": 1280, "height": 720}
    )
    yield context
    context.close()  # Required for video finalization


# ==============================
# PAGE FIXTURE
# ==============================
@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()


# ==============================
# TEST RESULT HOOK
# ==============================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Attach artifacts ONLY on test failure
    Delete everything if test passes
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when != "call":
        return

    page = item.funcargs.get("page", None)

    # --------------------------
    # TEST FAILED
    # --------------------------
    if rep.failed and page:
        test_name = item.nodeid.replace("::", "_").replace("/", "_")

        # 📸 Screenshot
        try:
            screenshot_path = SCREENSHOTS_DIR / f"{test_name}.png"
            page.screenshot(path=str(screenshot_path), full_page=True)

            allure.attach.file(
                str(screenshot_path),
                name="Screenshot on Failure",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print(f"⚠️ Screenshot capture failed: {e}")

        # 🎥 Video
        try:
            if page.video:
                video_path = page.video.path()

                allure.attach.file(
                    video_path,
                    name="Test Video",
                    attachment_type=allure.attachment_type.MP4
                )
        except Exception as e:
            print(f"⚠️ Video attach failed: {e}")

    # --------------------------
    # TEST PASSED → CLEANUP
    # --------------------------
    if rep.passed and page:
        # Delete video if exists
        try:
            if page.video:
                video_path = page.video.path()
                if os.path.exists(video_path):
                    os.remove(video_path)
        except Exception:
            pass
