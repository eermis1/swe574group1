from django.urls import path
from community.views import *

from community import feeds

app_name = 'community'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name="index"),
    path('search$', CommunitiesListTemplateView.as_view(), name="search-communities"),
    path('register', register_view, name="register"),
    path('login', login_view, name="login"),
    path('logout', logout_view, name="logout"),
    path('manager', CommunityLoginTemplateView.as_view(), name="manager"),
    path('communites-list', UserCommunitiesListTemplateView.as_view(), name="communities-list-user"),
    path('communities/<int:community_id>', CommunitiesDetailedTemplateView.as_view(), name="community-detail"),
    path('posts/<int:post_id>', PostsDetailedTemplateView.as_view(), name="post-detail"),
    path('data-types/<int:data_type_id>', DataTypeTemplateView.as_view(), name="data-type-detail"),
    path('communites-create', CreateCommunityTemplateView.as_view(), name="communities-create"),
    path('posts-create/<int:community_id>', CreatePostTemplateView.as_view(), name="posts-create"),
    path('data-type-create/<int:community_id>', CreateDataTypeTemplateView.as_view(), name="data-type-create"),
    path('join-community/<int:joined_community>', JoinCommunityTemplateView.as_view(), name="join-community"),
    path('joined-communites-list', JoinedCommunitiesListTemplateView.as_view(), name="joined-communities-list"),
    path('stream/json', feeds.UserJSONActivityFeed_V2.as_view(), name='actstream_feed_json'),
    path('stream/', notification, name='notification_combined'),
    path('stream/user/', notification_user, name='notification_user_all'),
    path('stream/community/', notification_community, name='notification_community_all'),
    path('stream/post', notification_post, name='notification_post_all'),
    path('followings/', followings, name='followings_combined'),
    path('followings/user/', followings_user, name='followings_user_all'),
    path('followings/community/', followings_community, name='followings_community_all'),
    path('followings/post/', followings_post, name='followings_post_all'),
    path('followers/', followers, name='followers'),
    path('flag-inappropriate', FlagPostAsInappropriate.as_view(), name="flag-post-inappropriate"),
    path('flag-appropriate', FlagPostAsAppropriate.as_view(), name="flag-post-appropriate")

]