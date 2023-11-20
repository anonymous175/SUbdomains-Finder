import sublist3r
import pyfiglet

py = pyfiglet.figlet_format("Subdomains finder")
py1 = "# By Umair Majeed  "

print(py)
print(py1)

#a=sublist3r.main('domain=',threads=400,ports="",savefile=False,verbose=True,enable_bruteforce=True,silent=False,engines=None)
a=sublist3r.main(input("\nEnter your Website: "),400,savefile=input("Enter Path to save output: "),ports=None,silent=False,verbose=True,enable_bruteforce=False,engines=None)
#print(str(a))
