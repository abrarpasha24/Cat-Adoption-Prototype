<h1>Pet-Adoption-Prototype</h1>

We will be setting up a DynamoDB table full of cats that are waiting to be adopted. When the adopted field is updated to true, a Lambda will be triggered that will send an email to the adoption center telling them that “[cat xyz] has been adopted!”

# Step-By-Step-Procedure
Stage 1 - Creating the DynamoDB table
Head to the DynamoDB dashboard: https://us-east-1.console.aws.amazon.com/dynamodbv2/home?#tables


![1](https://github.com/abrarpasha24/Pet-Adoption-Prototype/assets/30976576/3e67261c-78af-4755-99ec-64b0c8db4b33)

Stage 2 - Populating the table <br>
Now you get to add as many cats as you like to the cat-adoption table. In the real world this would be populated by an external service, or a frontend website the cat adoption agency uses, but in this case we will enter the data manually.

![2](https://github.com/abrarpasha24/Pet-Adoption-Prototype/assets/30976576/fbc0737b-8ba5-40e5-bef7-39a5ca5d8cad)


Stage 2a - Querying our data head to explore table items

![3](https://github.com/abrarpasha24/Pet-Adoption-Prototype/assets/30976576/a28aa44a-8c9d-4330-8a8f-6f7273e447cc)

Searching for “false” will return all cats that haven’t been adopted:

![4](https://github.com/abrarpasha24/Pet-Adoption-Prototype/assets/30976576/aa278073-5289-43c5-8425-7a23b5c2bf11)

Querying uses indexes, which is far more efficient and cost effective, without having this secondary index we would need to Scan the table to look for cats which are/aren’t adopted, which means DynamoDB iterates over every record and checks that key. With tables that have thousands or millions of records, this can be very expensive (and slow).

Stage 3 - Setting up SNS
Head to the SNS console: https://us-east-1.console.aws.amazon.com/sns/v3/home?region=us-east-1#/topics

![5](https://github.com/abrarpasha24/Pet-Adoption-Prototype/assets/30976576/839b623c-af43-419d-8bfa-00804dfc005d)

Stage 4 - Create the Lambda
Head to the Lambda console: https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/functions



In the Code tab, enter the following code:

![6](https://github.com/abrarpasha24/Pet-Adoption-Prototype/assets/30976576/e5862167-35e2-4fae-9149-dd2abc1299df)

This code basically iterates through all the records that DynamoDB passes to the Lambda function, and then publishes a message to SNS.

Don’t forget to click Deploy to save the function.

Stage 4a - Add DynamoDB permissions to the Lambda role

![7](https://github.com/abrarpasha24/Pet-Adoption-Prototype/assets/30976576/51977e85-bb9a-46d8-a5de-7354469a54b3)

This is required so the Lambda function can read from the DynamoDB Stream. In the real world this should be locked down a lot further, but in this case, we’re okay with the Lambda having full DynamoDB permissions to all tables.

Stage 5 - Enabling the DynamoDB Stream

![8](https://github.com/abrarpasha24/Pet-Adoption-Prototype/assets/30976576/a6b556fe-33be-4645-a4e6-ac6dd9fde3d8)

Stage 6 - Testing it out


Click on Explore table items

You should see the cat items you created earlier, if not, click on Scan → Run

Change one of the “adopted” fields to “true”

![9](https://github.com/abrarpasha24/Pet-Adoption-Prototype/assets/30976576/b9b98dc5-375f-4a0b-ad7f-5ecd6b4eb85b)

After a few seconds you should receive an email telling you that cat has been adopted!

![10](https://github.com/abrarpasha24/Pet-Adoption-Prototype/assets/30976576/3a89ca84-c1d6-40bc-b307-42e5e10af4b7)

Untitled

Stage 7 - Clean up

Most important!!!!! Make sure to clean-up all your resources

You’re all done!
