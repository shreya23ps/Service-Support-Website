from django.db import models


from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title

class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f'Comment by {self.name} on {self.blog_post}'
    

class Contact(models.Model):
    name = models.CharField(max_length=200)  # Field for the user's name
    email = models.EmailField()  # Field for the user's email
    subject = models.CharField(max_length=200)  # Field for the subject
    message = models.TextField()  # Field for the message

    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is created

    def _str_(self):
        return f"{self.name} - {self.subject}"  # String representation of the model
# Create your models here.

class Person(models.Model):
    aadhaar_number = models.CharField(max_length=12, primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    pan_number = models.CharField(max_length=10, unique=True, blank=True, null=True)
    is_alive = models.BooleanField(default=True)  # True for alive, False for deceased

    def __str__(self):
        return f"{self.name} {self.surname} - {self.aadhaar_number}"


class ElectoralRoll(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"Eligible Voter: {self.person.name} {self.person.surname}"


class PanCardApplication(models.Model):
    # Personal Details
    applicant_name = models.CharField(max_length=255)
    applicant_father_name = models.CharField(max_length=255)
    applicant_dob = models.DateField()
    applicant_gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    applicant_aadhaar = models.CharField(max_length=12, unique=True)
    
    # Contact Details
    applicant_address = models.TextField()
    applicant_email = models.EmailField()
    applicant_contact = models.CharField(max_length=15)
    
    # Identity and Address Proof Documents
    id_proof = models.FileField(upload_to='documents/id_proofs/')
    address_proof = models.FileField(upload_to='documents/address_proofs/')
    
    # Supporting Documents (Optional)
    documents = models.FileField(upload_to='documents/supporting_docs/', blank=True, null=True)
    
    # Timestamp for when the application was created
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"PAN Card Application for {self.applicant_name} {self.applicant_father_name}"
    

class DeathCertificateApplication(models.Model):
    # Personal details of the deceased
    deceased_name = models.CharField(max_length=255)
    deceased_dob = models.DateField()
    deceased_dod = models.DateField()  # Date of Death
    deceased_gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    deceased_aadhaar = models.CharField(max_length=12)  # Aadhaar No. (12 digits)
    deceased_address = models.TextField()

    # Applicant details
    applicant_name = models.CharField(max_length=255)
    applicant_relation = models.CharField(max_length=255)
    applicant_address = models.TextField()
    applicant_contact = models.CharField(max_length=15)
    applicant_email = models.EmailField(blank=True, null=True)

    # Supporting documents
    documents = models.FileField(upload_to='documents/supporting_docs/', null=True, blank=True)

    # Date of application
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Death Certificate Application for {self.deceased_name} by {self.applicant_name}"
    

class AddressChangeApplication(models.Model):
    applicant_name = models.CharField(max_length=200)
    applicant_dob = models.DateField()
    applicant_gender = models.CharField(max_length=20, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    applicant_aadhaar = models.CharField(max_length=12)  # Assuming Aadhaar is a 12-digit number

    old_address = models.TextField()
    new_address = models.TextField()

    address_proof = models.FileField(upload_to='documents/address_proofs/')
    additional_documents = models.FileField(upload_to='documents/supporting_docs', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Address Change Application for {self.applicant_name} ({self.applicant_aadhaar})"
    
class DrivingLicenseApplication(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    LICENSE_TYPE_CHOICES = [
        ('learner', "Learner's License"),
        ('permanent', 'Permanent License'),
    ]

    VEHICLE_CLASS_CHOICES = [
        ('mcwog', 'Motorcycle Without Gear'),
        ('mcwg', 'Motorcycle With Gear'),
        ('lmv', 'Light Motor Vehicle'),
        ('hmv', 'Heavy Motor Vehicle'),
    ]

    # Personal Details
    applicant_name = models.CharField(max_length=200)
    applicant_father_name = models.CharField(max_length=200)
    applicant_dob = models.DateField()
    applicant_gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    applicant_aadhaar = models.CharField(max_length=12)  # Aadhaar number (12 digits)
    applicant_address = models.TextField()

    # Driving License Details
    license_type = models.CharField(max_length=20, choices=LICENSE_TYPE_CHOICES)
    vehicle_class = models.CharField(max_length=20, choices=VEHICLE_CLASS_CHOICES)

    # Contact Details
    applicant_contact = models.CharField(max_length=15)
    applicant_email = models.EmailField()

    # Supporting Documents
    documents = models.FileField(upload_to='documents/supporting_docs/', null=True, blank=True)

    # Date of application
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant_name} - {self.license_type} Application"
    
class RationCardApplication(models.Model):
    applicant_name = models.CharField(max_length=255)
    applicant_father_name = models.CharField(max_length=255)
    applicant_dob = models.DateField()
    applicant_gender = models.CharField(max_length=10)
    applicant_aadhaar = models.CharField(max_length=12)
    applicant_address = models.TextField()
    applicant_state = models.CharField(max_length=100)
    applicant_district = models.CharField(max_length=100)
    applicant_city = models.CharField(max_length=100)
    applicant_pincode = models.CharField(max_length=6)
    applicant_email = models.EmailField()
    applicant_contact = models.CharField(max_length=15)
    id_proof = models.FileField(upload_to='documents/id_proofs/')
    address_proof = models.FileField(upload_to='documents/address_proofs/')
    photo = models.ImageField(upload_to='documents/photos/')
    family_members = models.IntegerField()
    ration_card_type = models.CharField(max_length=3, choices=[('APL', 'Above Poverty Line'), ('BPL', 'Below Poverty Line')])

    def __str__(self):
        return f"{self.applicant_name} - {self.ration_card_type}"
    
class VoterRegistration(models.Model):
    applicant_name = models.CharField(max_length=255)
    applicant_dob = models.DateField()
    applicant_gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    applicant_aadhaar = models.CharField(max_length=12, unique=True)
    applicant_address = models.TextField()
    applicant_pincode = models.CharField(max_length=6)
    applicant_email = models.EmailField()
    applicant_contact = models.CharField(max_length=15)
    id_proof = models.FileField(upload_to='documents/id_proofs/')
    address_proof = models.FileField(upload_to='documents/address_proofs/')

    def __str__(self):
        return f"{self.applicant_name} - {self.applicant_aadhaar}"