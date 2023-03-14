data "aws_iam_policy_document" "assume_role" {
    statement {
        actions = ["sts:AssumeRole"]
        effect = "Allow"
        principals {
            type = "Service"
            identifiers = ["ec2.amazonaws.com"]
        }
    }
}

data "aws_iam_policy_document" "ec2" {
    statement {
        effect = "Allow"
        actions = ["s3:*"]
        resources = ["arn:aws:s3:::*"]
    }
}

resource "aws_iam_role" "this" {
    name_prefix = "s3-access-role"
    assume_role_policy = data.aws_iam_policy_document.assume_role.json
    tags = {
        Name = "multiverse"
    }
}

resource "aws_iam_policy" "this" {
    name_prefix = "ec2-s3-access"
    path = "/"
    policy = data.aws_iam_policy_document.ec2.json
    tags = {
        Name = "multiverse"
    }
}

resource "aws_iam_policy_attachment" "this" {
    name = "ec2-s3-access"
    roles = [aws_iam_role.this.name]
    policy_arn = aws_iam_policy.this.arn
}

resource "aws_iam_instance_profile" "this" {
    name_prefix = "s3-access-role"
    role = aws_iam_role.this.name
}