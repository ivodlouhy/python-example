all: clean build package deploy

init:
	poetry install

build: init src/lambda/example/requirements.txt
	sam build

package:
	sam package \
		--template-file .aws-sam/build/template.yaml \
		--resolve-s3 \
		--output-template-file .aws-sam/build/template.packaged.yaml

deploy:
	sam deploy \
		--stack-name IvoDlouhyExample \
		--template-file .aws-sam/build/template.packaged.yaml \
		--resolve-s3 \
		--capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND \
		--on-failure DELETE \
		--parameter-overrides ExampleParameter=Hello! \
		--tags Project=Example

src/lambda/example/requirements.txt: pyproject.toml
	@poetry export -f requirements.txt --without-hashes --output $@

clean:
	rm -rf .aws-sam