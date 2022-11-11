SELECT category.category_title,  category_article_mapping.article_id
FROM category_article_mapping
LEFT JOIN category
ON category_article_mapping.category_id=category.category_id;

SELECT  category_article_mapping.category_title, article.owner_id
FROM category_article_mapping
LEFT JOIN article
ON category_article_mapping.article_id=article.article_id;

SELECT owner.owner_id, owner_owner_name, category_article_mapping.category_title
FROM owner
LEFT JOIN category_article_mapping
ON category_article_mapping.owner_id=owner.owner_id;

SELECT owner.owner_id, owner_owner_name, COUNT(DISTINCT owner.category_title)
from owner;