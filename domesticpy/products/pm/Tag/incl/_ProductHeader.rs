
Log.info('loading product %s (%s)' % \
    (<%-prod.getName()%>, <%-prod.getParams().fname%>))

l = Layer()
p = Page(<%-prod.getDuration()%>)
l.addPage(p)

