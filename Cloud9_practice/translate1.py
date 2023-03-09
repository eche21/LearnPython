# we need to tell python to use the boto3 package
import boto3

#we need to tell python which specific service we want to use within boto3
client = boto3.client('translate')

#the translate_text() method. declare the function using def, name, braces for parameters and a colon
def translate_text():
    response = client.translate_text(
        Text = 'I am learning to code in AWS',
        SourceLanguageCode= 'en',
        TargetLanguageCode='fr'
    )
    print(response)

def main():    
   translate_text()

if __name__== "__main__":
   main()