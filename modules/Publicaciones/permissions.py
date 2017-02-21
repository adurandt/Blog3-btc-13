from rest_framework import permissions 

class GroupPermission(permissions.BasePermission):
	message = "Usted no es parte de este grupo"
	SELECTED_GROUP = "Writers"

	def has_permission(self, request, view):  #overwrite

		if request.user.groups.filter(name=self.SELECTED_GROUP):
			return True 
		else:
			return False	
