import boto3

dynamobd = boto3.resource('dynamodb', region_name='us-east-1').Table('foodItems')


########################### Get and item ####################################
def get_item():
    response = dynamobd.get_item(
        Key={
            'ExpirationDate': '5/12/2020'
        }
    )
    item = response['Item'] # This will be in <class 'dict'>

    print(item)

########################### create and item #################################
def put_item():
    dynamobd.put_item(
        Item={
            "Category": "Rice",
            "ExpirationDate": "5/12/2020",
            "Food": "Brown Rice",
            "location": "Kitchen pantry",
            "NumberOfItems": "1"
        }
    )

get_item() # Output:{'Food': 'Apples', 'location': 'Kitchen fruit bowl', 'ExpirationDate': '5/12/2020', 'NumberOfItems': '2', 'Category': 'Fruit'}
put_item()
get_item() # Output: {'Food': 'Brown Rice', 'location': 'Kitchen pantry', 'ExpirationDate': '5/12/2020', 'NumberOfItems': '1', 'Category': 'Rice'}
           # Expected: {'Food': 'Apples', 'location': 'Kitchen fruit bowl', 'ExpirationDate': '5/12/2020', 'NumberOfItems': '2', 'Category': 'Fruit'},
           #           {'Food': 'Brown Rice', 'location': 'Kitchen pantry', 'ExpirationDate': '5/12/2020', 'NumberOfItems': '1', 'Category': 'Rice'}

# TODO: Need to rethink the primary key since it is suppose to be unique so that 
#       when you put_item with same ExpirationDate as other items they don't get 
#       overwritten