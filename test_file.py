# from django.db import models
#
#
# class User(models.Model):
#    nickname = models.CharField(
#       max_length=100,
#       unique=True,  # TODO: потом сделай уникальность регистронезависимым
#    )
#
#    profile_image = models.ImageField(upload_to='/avatars/')
#    password = models.TextField()
#
#
# class Comment(models.Model):
#    description = models.TextField()
#    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#
# class Like(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#    publication = models.ManyToManyField()
#
# class Publication(models.Model):
#    image = models.ImageField(upload_to='/publication_images/')
#    description = models.TextField(null=True)
#    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publications')
#    comment = models.ForeignKey(Comment, null=True)
#
#
