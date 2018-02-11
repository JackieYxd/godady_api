# godady_api
 Call GoDaddy API ， statistical domain name information
 
### 首先，能正常使用api的前提是你已经购买了域名。
### 第二，如果不熟悉godaddy的调用过程，官方也给了详细的步骤与使用的说明文档。
![](http://img.blog.csdn.net/20180211164452628?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbW9uX3N0YXI=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
### 第三，需要获取api的认证，在这里点击 `Getting Access` 是key与secret。注意，其中的Test无法使用的，需要用产品的key与对应的secret才可以。而且，一旦选择创建key之后，里面的secret只会出现一次，所以好好保存。
![这里写图片描述](http://img.blog.csdn.net/20180211164914740?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbW9uX3N0YXI=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
### 第四，查阅api的官方文档，熟悉每个api的作用。
其中使用的最多的应该也就是/v1/domains 这个系列的api了，所以如果有需要，多了解。
 ![这里写图片描述](http://img.blog.csdn.net/20180211165525299?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbW9uX3N0YXI=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
 
 - **注意：**
  **这里，godaddy官方只提供了api的借口，对于python使用的第三方库是没有的。所以只能自己搜或者自己写。我比较推荐的是godaddypy，这里也使用的是这个库。**

----------

#### 我们的需求：

 -  **将对应账户里面的所有域名提取出来，然后打印出每个域名对应的创建时间，截止时间，公司信息，是否自动续费和域名状态。**
