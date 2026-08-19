# AWS_LAMBDA_CICD
ALL THE CODE I PUSH IN GITHUB, IT WILL CREATE A LAMBDA FUNCTION AND TRIGGER THE EVENT AUTOMATICALLY



python3 -m venv .venv  
source .venv/bin/activate

##creating and moving to test branch 
git checkout -b test

git push -u origin test
            │      │
            │      └── branch = test
            │
            └───────── remote GitHub repository = origin