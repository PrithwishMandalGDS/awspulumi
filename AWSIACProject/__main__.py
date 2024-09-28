import pulumi
import pulumi_aws as aws

assume_role_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": "sts:AssumeRole",
            "Principal": {
                "Service": "ec2.amazonaws.com"
            },
            "Effect": "Allow",
            "Sid": ""
        }
    ]
}

iam_role = aws.iam.Role("myRole",assume_role_policy=pulumi.Output.from_input(assume_role_policy))

pulumi.export("role_name", iam_role.name)
