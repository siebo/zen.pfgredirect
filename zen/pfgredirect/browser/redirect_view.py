from Products.Five.browser import BrowserView

class RedirectView(BrowserView):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        "Redirect to provided URL"
        redirectURL = self.context.getRedirectURL()
        response = self.request.response
        return response.redirect(redirectURL)
