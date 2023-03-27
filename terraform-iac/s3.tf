resource "aws_s3_bucket" "this" {
    bucket_prefix = "app-kai-jones"
    force_destroy = true
    tags = {
        Name = "Survey App Bucket"
    }
}

resource "aws_s3_bucket_acl" "this" {
    bucket = aws_s3_bucket.this.id
    acl = "private"
}

resource "aws_s3_object" "this" {
    bucket = aws_s3_bucket.this.id
    key = "results.csv"
    source = "${path.module}/results.csv"
    etag = filemd5("${path.module}/results.csv")
}

resource "aws_s3_object" "test_file" {
    bucket = aws_s3_bucket.this.id
    key = "test_file.txt"
    content = "hello world!!"
}