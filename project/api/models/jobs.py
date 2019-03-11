# project/api/models/quotes.py
from marshmallow import Schema, fields, ValidationError, pre_load
from project.api.models.users import UserSchema

from project import db
import datetime


class Job(db.Model):
    __tablename__ = "job"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    posted_at = db.Column(db.DateTime)
    is_deleted = db.Column(db.Integer, nullable=False)
    # posts = db.relationship('Post', backref='author', lazy='dynamic')
    # jobdetail = db.relationship('JobDetail', primaryjoin="Job.id==JobDetail.job_id")
    # boston_addresses = db.relationship("Address",
    #                                 primaryjoin="and_(User.id==Address.user_id, "
    #                                             "Address.city=='Boston')")

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # jobdetail = db.relationship(
    #     'JobDetail',
    #     backref=db.backref('JobDetail', primaryjoin="Job.id==JobDetail.job_id"),
    # )
    user = db.relationship(
        'User',
        backref=db.backref('jobs', lazy='dynamic'),
    )

    def __init__(self, data):
        self.is_deleted = 0
        self.posted_at = datetime.datetime.utcnow()
        self.title = data[0]['title']

    def __repr__(self):
        return '{}-{}-{}'.format(self.title, self.is_deleted, self.posted_at)

class JobDetail(db.Model):
    __tablename__ = "job_detail"
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String, nullable=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
    url = db.Column(db.String, nullable=True)
    thubnail = db.Column(db.String, nullable=True)
    image_name = db.Column(db.String, nullable=True)

    def __repr__(self):
        return 'desc:{}-jobId:{}-URL:{}-thubnail:{}-imageName:{}'.format(self.desc, self.job_id, self.url, self.thubnail, self.image_name)


# Custom validator
def must_not_be_blank(data):
    if not data:
        raise ValidationError('Data not provided.')


class JobDetailSchema(Schema):
    id = fields.Int(dump_only=True)
    desc = fields.Str(required=True, validate=must_not_be_blank)
    url = fields.Str()
    thubnail = fields.Str()
    image_name = fields.Str()

class JobSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True, validate=must_not_be_blank)
    posted_at = fields.DateTime(dump_only=True)
    is_deleted = fields.Int(dump_only=True)
    jobdetail = fields.Nested(JobDetailSchema)
    user_id = fields.Int()
    user = fields.Nested(UserSchema)

    @pre_load
    def process_job_detail(self, data):
        job_detail = data.get('job_detail')
        data['job_detail'] = job_detail[0]
        return data






