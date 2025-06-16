# AWS CloudFormation Notes

## Core Concepts
- **Templates**: JSON or YAML files that describe AWS resources
- **Stacks**: Collection of AWS resources created and managed as a single unit
- **Change Sets**: Preview of proposed changes before updating a stack
- **StackSets**: Manage stacks across multiple accounts and regions

## Workflow
1. **Template Development**
   - Write CloudFormation template (YAML/JSON)
   - Define resources, parameters, and outputs
   - Test template syntax and validation
   - Use AWS SAM for serverless applications

2. **Build**
   - Build application code and dependencies
   - Prepare source code for packaging

3. **Package**
   - Package artifacts (Lambda functions, layers)
   - Upload to S3 bucket for deployment
   - Generate packaged template

4. **Deploy**
   - Create/update CloudFormation stack
   - Review change set (if updating)
   - Monitor deployment progress
   - Verify resource creation
   - Check outputs and logs

5. **Maintenance**
   - Monitor stack health
   - Update resources as needed
   - Manage drift detection
   - Clean up unused resources

## Key Features
- **Infrastructure as Code (IaC)**: Define infrastructure in code
- **Declarative**: Describe what you want, not how to do it
- **Automated Deployment**: Consistent and repeatable deployments
- **Rollback Capability**: Automatic rollback on failure
- **Resource Dependencies**: Automatic handling of resource creation order
- **Parameter Store**: Store and reference sensitive information
- **Custom Resources**: Extend functionality with custom logic

## Template Components
- **Parameters**: Input values for templates
- **Resources**: AWS resources to create
- **Mappings**: Key-value pairs for conditional values
- **Outputs**: Values returned after stack creation
- **Conditions**: Control resource creation based on conditions
- **Metadata**: Additional information about resources
- **Transform**: Serverless application model (SAM) transforms

## Best Practices
- Use nested stacks for complex architectures
- Implement proper IAM roles and permissions
- Use parameter constraints for input validation
- Implement proper error handling
- Use tags for resource organization
- Follow security best practices
- Implement proper logging and monitoring

## Resources
- [AWS CloudFormation Template Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-template-resource-type-ref.html)
- [AWS CloudFormation Best Practices](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html)
- [AWS CloudFormation Sample Templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-sample-templates.html) 