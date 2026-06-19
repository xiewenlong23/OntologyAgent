<!-- BILINGUAL -->
> Source: https://www.palantir.com/docs/foundry/object-explorer/pivot-linked/
---
# Pivot to explore linked objects
在执行 exploration 时，可以将 exploration 的主 object type 切换到任何 linked object type。下面我们通过一个具体的示例来看一下。

While performing an exploration, it is possible to shift the main object type of your exploration to any linked object type. Let’s look at this through a specific example below.
如何查找未来 30 天内从美国东部大型机场起飞的全部航班？

How do I find all flights departing in the next 30 days from large airports in the Eastern United States?
值得注意的是，可以通过从 **Flights** 的 exploration 入手，并根据其 linked airports 的属性进行筛选来实现这一点 [在 Linked Properties 上进行筛选](/docs/foundry/object-explorer/explore-charts/#charts-on-linked-objects)。话虽如此，另一种回答该问题的方式是从 **Airports** 的 exploration 入手，并将这些 airports 筛选为仅包含位于美国东部且拥有大量独立承运商的机场：

Notably, it is possible to achieve this by starting with an exploration of **Flights**, and filtering on the attributes of their linked airports [Filtering on Linked Properties](/docs/foundry/object-explorer/explore-charts/#charts-on-linked-objects). That said, another way to answer this question is by starting with an exploration of **Airports**, and filtering these airports to only those in the Eastern US with a high number of unique carriers:

> 📷 **[图片: Exploration on Airports]**

> 📷 **[图片: Exploration on Airports]**

从这里，我们现在想要 **pivot**（透视）到关联的 **Departing Flights**。我们可以通过点击右下角 "Linked Objects" 部分中的相应选项来实现此操作。这样做会将我们 exploration 的主 object type 更改为 **Flights**，并将筛选范围限定为仅包含此前筛选出的美国东部大型机场起飞的航班：

From here, we now want to **pivot** to the associated **Departing Flights**. We can do so by clicking on this option in the “Linked Objects” section in the bottom-right. Doing so will change the main object type of our exploration to be **Flights**, and filter us to only those flights departing from the large, eastern airports that we had filtered down to previously:

> 📷 **[图片: Exploration Pivoted to Flights]**

> 📷 **[图片: Exploration Pivoted to Flights]**

如上所述，我的 exploration 的 **results**（结果）现在不再是 Airports，而是 Flights（您可以从右侧的预览面板中看到）。可以通过多个 link 进行多次 pivot，从而允许您灵活地跨 ontology 进行探索。

The **results** of my exploration above are now no longer the Airports, but are instead the Flights (as you can see from the preview panel to the right). It is possible to pivot through multiple links, thus allowing you to flexibly explore across the ontology.