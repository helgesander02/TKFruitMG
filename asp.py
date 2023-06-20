import aspose.words as aw
from datetime import datetime
doc = aw.Document()
builder = aw.DocumentBuilder(doc)

# comment = aw.Comment(doc)
# comment.author = "John Doe"
# comment.initial = "JD"
# comment.date_time = datetime.now()
# comment.set_text("Quisque fringilla leo.")

para = doc.first_section.body.first_paragraph
para2 = doc.first_section.body.first_paragraph
# para.append_child(aw.CommentRangeStart(doc, comment.id))
para.append_child(aw.Run(doc, "Morbi enim nunc faucibus a."))
para2.append_child(aw.Run(doc, "測試中文亂碼"))
# para.append_child(aw.CommentRangeEnd(doc, comment.id))
# para.append_child(comment)
builder.writeln("就只是測試")
builder.writeln("還是測試")
# comment.add_reply("Jane Doe", "JD", datetime.now(), "Pellentesque vel sapien justo.")

doc.save("Output.pdf")

