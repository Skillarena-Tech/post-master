import boto3


class DynamoDBUtility:
    def __init__(self, table_name:str, primary_key:str
                 , sort_key:str=None, sort_key_type:str=None):
        self.table_name = table_name
        self.primary_key = primary_key
        self.sort_key = sort_key
        self.sort_key_type = sort_key_type
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(self.table_name)

    def get_all(self) -> list:
        try:
            resp = self.table.scan()
            result = resp.get('Items')
            
            while 'LastEvaluatedKey' in resp:
                resp = self.table.scan(ExclusiveStartKey=resp['LastEvaluatedKey'])
                result.extend(resp['Items'])
            return result
        except Exception as e:
            return []

    def get_by_primary_key(self, key) -> dict:
        try:
            resp = self.table.get_item(Key={self.primary_key: key})
            result = resp.get('Item')
            return result
        except Exception as e:
            return {}

    def create(self, data) -> bool:
        try:
            self.table.put_item(Item=data)
            return True
        except Exception as e:
            return False

    def update(self, key , data:dict) -> bool:
        try:
            update_expression, expression_attribute_values = self.generate_update_expression(data)
            self.table.update_item( Key={self.primary_key: key}, 
                                    UpdateExpression=update_expression, 
                                    ExpressionAttributeValues=expression_attribute_values)
            return True
        except Exception as e:
            return False

    def delete(self, key)->bool:
        try:
            self.table.delete_item(Key={self.primary_key: key})
            return True
        except Exception as e:
            return False

    @staticmethod
    def generate_update_expression(update_values:dict) -> (str, dict):

        update_expression = "SET "
        expression_attribute_values = {}

        for key, value in update_values.items():
            placeholder = f":{key.replace('.', '_')}"
            update_expression += f"{key} = {placeholder}, "
            expression_attribute_values[placeholder] = value

        update_expression = update_expression.rstrip(", ")
        return update_expression, expression_attribute_values
