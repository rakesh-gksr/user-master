import datetime

from project.api.utils import authenticate
from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from project import db
import pprint

from project.api.models.jobs import JobSchema, Job, JobDetail, JobDetailSchema
from project.api.models.users import User

job_schema = JobSchema()
job_detail_schema = JobDetailSchema()
job_details_schema = JobDetailSchema(many=True, only=('id', 'job.title', 'desc'))
jobs_schema = JobSchema(many=True, only=('id', 'title', 'is_deleted'))

##### API #####
jobs_blueprint = Blueprint('jobs', __name__)


@jobs_blueprint.route('/jobs/', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    result = jobs_schema.dump(jobs, many=True)
    return jsonify({'jobs': result})


@jobs_blueprint.route('/jobs/<int:pk>', methods=['GET'])
def get_job(pk):
    try:
        job = Job.query.get(pk)
    except :
        return jsonify({'message': 'Job could not be found.'}), 400
    result = job_schema.dump(job)
    return jsonify({'job': result})


@jobs_blueprint.route('/jobs', methods=['POST'])
# @authenticate
def new_job():
    user = User.query.filter_by(id=int(1)).first()

    json_data = request.get_json()
    print "json_data==>",json_data
    if not json_data:
        return jsonify({'message': 'No input data provided'}), 400
    # Validate and deserialize input
    try:
        data = job_detail_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 422

    job = Job(data)
    db.session.add(job)
    job_detail = JobDetail(
        desc=data[0]['desc'],
        job=job,
        user=user,
        url = data[0]['url'],
        thubnail = data[0]['thubnail'],
        image_name = data[0]['image_name'],
    )
    db.session.add(job_detail)
    db.session.commit()
    result = job_detail_schema.dump(JobDetail.query.get(job_detail.id))
    return jsonify({
        'message': 'Created new job.',
        'job': result,
    })

@jobs_blueprint.route('/job-detail-list/', methods=['GET'])
def get_job_details():
    jobs = JobDetail.query.all()
    result = job_details_schema.dump(jobs, many=True)
    return jsonify({'jobs': result})
