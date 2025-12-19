import allure
import pytest
import os
import shutil
from pathlib import Path


@pytest.fixture(scope="function")
def context(browser, request):
    context = browser.new_context(
        record_video_dir="videos/",
        record_video_size={"width": 1280, "height": 720}
    )
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)

        if page:
            # Screenshot
            screenshot = page.screenshot(full_page=True)
            allure.attach(
                screenshot,
                name="Screenshot on Failure",
                attachment_type=allure.attachment_type.PNG
            )

            # Page HTML
            allure.attach(
                page.content(),
                name="Page Source",
                attachment_type=allure.attachment_type.HTML
            )

        # Attach video (pass or fail)
        if page.video:
            video_path = page.video.path()
            if os.path.exists(video_path):
                allure.attach.file(
                    video_path,
                    name="Test Video",
                    attachment_type=allure.attachment_type.MP4
                )
@pytest.fixture(scope="session", autouse=True)
def clean_videos_folder():
    videos_dir = Path("videos")
    if videos_dir.exists():
        shutil.rmtree(videos_dir)
    videos_dir.mkdir(exist_ok=True)