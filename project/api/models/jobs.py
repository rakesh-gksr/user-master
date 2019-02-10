# project/api/models/quotes.py
from marshmallow import Schema, fields, ValidationError, pre_load

from project import db
import datetime


class Job(db.Model):
    __tablename__ = "job"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    posted_at = db.Column(db.DateTime)
    is_deleted = db.Column(db.Integer, nullable=False)

    def __init__(self, data):
        self.is_deleted = 0
        self.posted_at = datetime.datetime.utcnow()
        self.title = data[0]['job']['title']


class JobDetail(db.Model):
    __tablename__ = "job_detail"
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String, nullable=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    url = db.Column(db.String, nullable=True)
    thubnail = db.Column(db.String, nullable=True)
    image_name = db.Column(db.String, nullable=True)
    job = db.relationship(
        'Job',
        backref=db.backref('job', lazy='dynamic'),
    )
    user = db.relationship(
        'User',
        backref=db.backref('users', lazy='dynamic'),
    )



# Custom validator
def must_not_be_blank(data):
    if not data:
        raise ValidationError('Data not provided.')


class JobSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True, validate=must_not_be_blank)
    posted_at = fields.DateTime(dump_only=True)
    is_deleted = fields.Int(dump_only=True)


class JobDetailSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int()
    desc = fields.Str(required=True, validate=must_not_be_blank)
    url = fields.Str()
    thubnail = fields.Str()
    image_name = fields.Str()
    job = fields.Nested(JobSchema)

    @pre_load
    def process_job(self, data):
        job = data.get('job')
        data['job'] = job[0]
        return data




