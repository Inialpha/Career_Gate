from calendly.client import Client
client = Client('eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNzAyMTIxODg2LCJqdGkiOiIwZjY5ZDExMS04ZjVkLTRmNjUtYTBhZS1jYmU2ZGM5ODdjZWIiLCJ1c2VyX3V1aWQiOiJhNzM4NjE3ZS0wNmE4LTQ4ZTAtOGYwYS03ZjI4MmIzZmUwOTEifQ.N4PYJ91tC1g5_Ow6ZcGej8Irid3PSFVFqS39dhB-_0cpvvmuQAXWGvW1552V7u_g7wmjidIhjYT15VPindG-JA')

user_uri = client.user_uri

user_uuid = client.user_uuid
organization_uri = client.organization_uri
organization_uuid = client.organization_uuid
print('user_uri:  ', user_uri)
print('user_uuid:  ',  user_uuid)
print('organization_uri:  ', organization_uri)
print('organization_uuid:  ', organization_uuid)

client = Client(client_id="x8C64k5ruaayfCaBXGs_ZEE3hZKb2j2K3vGYdu06ddA", client_secret="VoQtwz2AmNw8uGex4uNLbr56m9l5bbY8HqYu-hnAFC0", redirect_uri="")

print(client)
