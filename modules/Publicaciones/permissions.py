from rest_framework import permission 

class GroupPersmission(permissions.BasePermission):
	message = "Usted no es parte de este grupo"

	def has_permission(self, request, view):  #overwrite

		if request.user.groups == "Writers":
			return True 
		else:
			return False	
