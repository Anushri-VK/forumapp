from django.urls import path
from forumapp.views import dashboard,questions,discussion,upvote,signout


urlpatterns = [
	path("dashboard/",dashboard),
	path("questions/",questions),
	path("discussion/<int:question_id>/",discussion),
	path("upvote/<int:answer_id>/",upvote),
	path("signout/",signout),
	# path("discussion/<int:discussion_id>/",discussion),
	

]