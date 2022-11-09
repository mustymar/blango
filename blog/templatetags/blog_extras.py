from django import template
from django.contrib.auth import get_user_model
from django.utils.html import html
from django.utils.safestring import mark_safe
from django.utils.html import format_html

register = template.Library()
User = get_user_model()

@register.filter(name="author_details")
def author_details(author, current_user):
  if not isinstance(author, User):
    return ""

  if author == current_user:
    return format_html("<strong>Me</strong>")
    
  if author.first_name and author.last_name:
    name = f"{author.first_name} {author.last_name}"
  
  else:
    name = f"{author.username}"

  if author.email:
    email = author.email
    prefix = format_html("<a href='mailto:{}'>", author.email)
    suffix = format_html("</a>")

  else:
    prefix = ""
    suffix = ""

  return format_html("{}{}{}", prefix, name, suffix)


