from taipy.gui import Markdown
import taipy as tp
from taipy.core.job.job import Job
from config.pipelines import pipeline_train
from models.data import initial_dataset


def job_status_changed(pipeline, job: Job):
    print(job.status)


def training_button_clicked(state, id, action):
    pipeline = tp.create_pipeline(pipeline_train)
    # Set initial dataset:
    pipeline.initial_dataset.write(initial_dataset)
    tp.subscribe_pipeline(
        pipeline=pipeline,
        callback=job_status_changed,
    )
    tp.submit(pipeline)


page = Markdown("src/pages/home.md")
