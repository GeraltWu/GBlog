from fastapi import APIRouter
from app.routers.front import articles, moments, about, comments, site, auth # 添加 about 模块

router = APIRouter(prefix="/front", tags=["前台"])

router.include_router(articles.router, tags=["前台-文章"])
router.include_router(comments.router, tags=["前台-评论"])  # 添加评论路由
router.include_router(moments.router, tags=["前台-动态"])
router.include_router(about.router, tags=["前台-关于"])  # 添加关于路由
router.include_router(site.router, tags=["前台-网站"])
router.include_router(auth.router, tags=["前台-认证"])  # 添加关于路由
