#Practical
name=input("What\'s Your Name?").strip().capitalize()
email=input("What\'s Your E-mail?").strip()
print(f"Hello {name} Your E-mail Is {email}")
username=email[:email.index("@")]
website=email[email.index("@")+1:]
print(f"Your User_name {username} Your Web Is {website}")
print("#"*30)
#########################################################
age=int(input("What\'s Your Age").strip())
months=age*12
weeks=months*4
days=age*365
hours=days*24
minu=hours*60
sec=minu*60
print('You Lived For:')
print(f"{months} Months.")
print(f"{weeks:,} Weeks.")
print(f"{days:,} Days.")
print(f"{hours:,} Hours.")
print(f"{minu:,} Minutes.")
print(f"{sec:,} Seconds.")