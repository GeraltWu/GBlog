/*
Navicat MySQL Data Transfer

Source Server         : blog
Source Server Version : 80032
Source Host           : localhost:3306
Source Database       : blog

Target Server Type    : MYSQL
Target Server Version : 80032
File Encoding         : 65001

Date: 2025-05-07 10:53:26
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for about
-- ----------------------------
DROP TABLE IF EXISTS `about`;
CREATE TABLE `about` (
  `id` bigint NOT NULL,
  `name_en` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `name_zh` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `value` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of about
-- ----------------------------
INSERT INTO `about` VALUES ('1', 'title', '标题', 'WHO AM I');
INSERT INTO `about` VALUES ('2', 'musicId', '网易云歌曲ID', '2001051777');
INSERT INTO `about` VALUES ('3', 'content', '正文Markdown', '<h2>这是一个h2标题</h2><p>这是一个p正文</p>');
INSERT INTO `about` VALUES ('4', 'commentEnabled', '评论开关', 'true');

-- ----------------------------
-- Table structure for blog
-- ----------------------------
DROP TABLE IF EXISTS `blog`;
CREATE TABLE `blog` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '文章标题',
  `first_picture` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '文章首图，用于随机文章展示',
  `content` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '文章正文',
  `description` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '描述',
  `is_published` bit(1) NOT NULL COMMENT '公开或私密',
  `is_recommend` bit(1) NOT NULL COMMENT '推荐开关',
  `is_appreciation_enabled` bit(1) NOT NULL COMMENT '赞赏开关',
  `is_comment_enabled` bit(1) NOT NULL COMMENT '评论开关',
  `is_private` bit(1) NOT NULL,
  `is_top` bit(1) NOT NULL COMMENT '是否置顶',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `update_time` datetime NOT NULL COMMENT '更新时间',
  `views` int NOT NULL COMMENT '浏览次数',
  `words` int NOT NULL COMMENT '文章字数',
  `read_time` int NOT NULL COMMENT '阅读时长(分钟)',
  `category_id` bigint NOT NULL COMMENT '文章分类',
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '密码保护',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `type_id` (`category_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of blog
-- ----------------------------
INSERT INTO `blog` VALUES ('1', '啊啊', 'asd', 'aaa', 'aaa', '', '', '', '', '\0', '', '2025-04-27 12:59:14', '2025-04-27 12:59:18', '71', '1', '11', '1', '');
INSERT INTO `blog` VALUES ('2', 'My First Blog Post', 'https://example.com/images/blog1.jpg', 'This is the detailed content of the first blog post.', 'This post introduces the basics of starting a blog.', '', '', '', '', '\0', '\0', '2025-01-15 10:00:00', '2025-01-15 10:00:00', '501', '1000', '5', '1', null);
INSERT INTO `blog` VALUES ('3', 'How to Cook Pasta', 'https://example.com/images/blog2.jpg', 'Detailed steps on how to cook perfect pasta.', 'A guide for cooking enthusiasts.', '', '\0', '\0', '', '\0', '\0', '2025-02-20 08:30:00', '2025-02-20 08:30:00', '309', '800', '4', '1', null);
INSERT INTO `blog` VALUES ('4', 'Private Thoughts', 'https://example.com/images/private.jpg', 'This is a private post containing personal reflections.', 'Personal reflections not for public viewing.', '', '\0', '\0', '\0', '', '\0', '2025-03-05 16:45:00', '2025-03-05 16:45:00', '2', '600', '3', '1', 'secret123');

-- ----------------------------
-- Table structure for blog_tag
-- ----------------------------
DROP TABLE IF EXISTS `blog_tag`;
CREATE TABLE `blog_tag` (
  `blog_id` bigint NOT NULL,
  `tag_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of blog_tag
-- ----------------------------
INSERT INTO `blog_tag` VALUES ('1', '1');

-- ----------------------------
-- Table structure for category
-- ----------------------------
DROP TABLE IF EXISTS `category`;
CREATE TABLE `category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `category_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of category
-- ----------------------------
INSERT INTO `category` VALUES ('1', '学习');

-- ----------------------------
-- Table structure for city_visitor
-- ----------------------------
DROP TABLE IF EXISTS `city_visitor`;
CREATE TABLE `city_visitor` (
  `city` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '城市名称',
  `uv` int NOT NULL COMMENT '独立访客数量',
  PRIMARY KEY (`city`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of city_visitor
-- ----------------------------
INSERT INTO `city_visitor` VALUES ('Chicago', '800');
INSERT INTO `city_visitor` VALUES ('Los Angeles', '1200');
INSERT INTO `city_visitor` VALUES ('New York', '1500');

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nickname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '昵称',
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '邮箱',
  `qq` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '如果评论昵称为QQ号，则将昵称和头像置为QQ昵称和QQ头像，并将此字段置为QQ号备份',
  `avatar` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '头像(图片路径)',
  `ip` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '评论者ip地址',
  `website` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '个人网站',
  `content` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '评论内容',
  `create_time` datetime DEFAULT NULL COMMENT '评论时间',
  `is_published` bit(1) NOT NULL COMMENT '公开或回收站',
  `is_admin_comment` bit(1) NOT NULL COMMENT '博主回复',
  `page` int NOT NULL COMMENT '0普通文章，1关于我页面，2友链页面',
  `is_notice` bit(1) NOT NULL COMMENT '接收邮件提醒',
  `blog_id` bigint DEFAULT NULL COMMENT '所属的文章',
  `root_comment_id` bigint NOT NULL COMMENT '所属根评论id，顶级评论为-1',
  `parent_comment_id` bigint NOT NULL COMMENT '父评论id，-1为根评论',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of comment
-- ----------------------------
INSERT INTO `comment` VALUES ('1', 'John Doe', 'john@example.com', null, '/img/comment-avatar/1.jpg', '192.168.1.1', 'https://johndoe.com', 'Great post! Really enjoyed reading it.', '2025-01-16 11:30:00', '', '\0', '0', '', '1', '-1', '-1');
INSERT INTO `comment` VALUES ('2', 'Admin', 'admin@example.com', null, '/img/comment-avatar/2.jpg', '192.168.1.2', 'https://adminblog.com', 'Thank you for your kind words!', '2025-01-17 09:45:00', '', '\0', '0', '\0', '1', '1', '1');
INSERT INTO `comment` VALUES ('3', 'Jane Smith', 'jane@example.com', null, '/img/comment-avatar/3.jpg', '192.168.2.1', null, 'I have a question about the cooking time.', '2025-02-21 14:20:00', '', '\0', '0', '', '1', '1', '2');
INSERT INTO `comment` VALUES ('4', 'John Doe', 'john@example.com', null, '/img/comment-avatar/4.jpg', '192.168.1.1', 'https://johndoe.com', 'Great post! Really enjoyed reading it.', '2025-01-16 11:30:00', '', '\0', '0', '', '1', '1', '2');
INSERT INTO `comment` VALUES ('5', 'Admin', 'admin@example.com', null, '/img/comment-avatar/5.jpg', '192.168.1.2', 'https://adminblog.com', 'Thank you for your kind words!', '2025-01-17 09:45:00', '', '', '0', '\0', '1', '1', '2');
INSERT INTO `comment` VALUES ('6', 'Jane Smith', 'jane@example.com', null, '/img/comment-avatar/6.jpg', '192.168.2.1', null, 'I have a question about the cooking time.', '2025-02-21 14:20:00', '', '\0', '1', '', null, '-1', '-1');
INSERT INTO `comment` VALUES ('7', 'John Doe', 'john@example.com', null, '/img/comment-avatar/5.jpg', '192.168.1.1', 'https://johndoe.com', 'Great post! Really enjoyed reading it.', '2025-01-16 11:30:00', '', '\0', '1', '', null, '6', '6');
INSERT INTO `comment` VALUES ('8', 'Admin', 'admin@example.com', null, '/img/comment-avatar/4.jpg', '192.168.1.2', 'https://adminblog.com', 'Thank you for your kind words!', '2025-01-17 09:45:00', '', '', '1', '\0', null, '6', '7');
INSERT INTO `comment` VALUES ('9', 'Jane Smith', 'jane@example.com', null, '/img/comment-avatar/3.jpg', '192.168.2.1', null, 'I have a question about the cooking time.', '2025-02-21 14:20:00', '', '\0', '0', '', '2', '-1', '-1');
INSERT INTO `comment` VALUES ('10', '通浩宇', 'k7nggq.lfs@sina.com', null, '/img/comment-avatar/2.jpg', '', 'enim', 'testest', '2025-04-30 09:55:20', '', '\0', '0', '', '1', '1', '2');
INSERT INTO `comment` VALUES ('11', 'wer', 'wer@123.com', null, '/img/comment-avatar/1.jpg', '', '', '@[BanGDream_香澄-期待]@[BanGDream_香澄-期待]@[BanGDream_香澄-期待]', '2025-04-30 15:22:34', '', '\0', '0', '', '1', '-1', '-1');
INSERT INTO `comment` VALUES ('12', 'wer', 'wer@123.com', null, '/img/comment-avatar/6.jpg', '', '', '@[tieba_呵呵]', '2025-04-30 15:26:45', '', '\0', '0', '', '1', '-1', '-1');
INSERT INTO `comment` VALUES ('13', 'wer', 'wer@123.com', null, '/img/comment-avatar/5.jpg', '', '', '@[BanGDream_有咲-汗]@[BanGDream_有咲-汗]', '2025-04-30 15:28:09', '', '\0', '0', '', '1', '12', '12');
INSERT INTO `comment` VALUES ('14', 'wer', 'wer@123.com', null, '/img/comment-avatar/1.jpg', '', '', '@[BanGDream_香澄-期待]@[BanGDream_香澄-期待]', '2025-05-01 16:19:07', '', '\0', '1', '', null, '-1', '-1');
INSERT INTO `comment` VALUES ('15', 'wer', 'wer@123.com', null, '/img/comment-avatar/5.jpg', '', '', '@[BanGDream_LOCK-不可以]@[BanGDream_LOCK-不可以]测试', '2025-05-01 16:49:09', '', '\0', '1', '', null, '6', '8');

-- ----------------------------
-- Table structure for exception_log
-- ----------------------------
DROP TABLE IF EXISTS `exception_log`;
CREATE TABLE `exception_log` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `uri` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '请求接口',
  `method` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '请求方式',
  `param` varchar(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '请求参数',
  `description` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '操作描述',
  `error` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci COMMENT '异常信息',
  `ip` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT 'ip',
  `ip_source` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT 'ip来源',
  `os` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '操作系统',
  `browser` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '浏览器',
  `create_time` datetime NOT NULL COMMENT '操作时间',
  `user_agent` varchar(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT 'user-agent用户代理',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of exception_log
-- ----------------------------
INSERT INTO `exception_log` VALUES ('1', '/api/blog/1', 'GET', '', 'Fetching blog post 1', 'Database connection error', '192.168.1.3', 'New York', 'Windows 10', 'Chrome', '2025-01-15 10:05:00', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36');
INSERT INTO `exception_log` VALUES ('2', '/api/comments', 'POST', 'nickname=Test&email=test@example.com&content=Test comment', 'Posting a new comment', 'Invalid email format', '192.168.1.4', 'Los Angeles', 'macOS', 'Firefox', '2025-02-20 08:35:00', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0');
INSERT INTO `exception_log` VALUES ('3', '/api/blog/1', 'GET', '', 'Fetching blog post 1', 'Database connection error', '192.168.1.3', 'New York', 'Windows 10', 'Chrome', '2025-01-15 10:05:00', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36');
INSERT INTO `exception_log` VALUES ('4', '/api/comments', 'POST', 'nickname=Test&email=test@example.com&content=Test comment', 'Posting a new comment', 'Invalid email format', '192.168.1.4', 'Los Angeles', 'macOS', 'Firefox', '2025-02-20 08:35:00', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0');
INSERT INTO `exception_log` VALUES ('5', '/api/blog/1', 'GET', '', 'Fetching blog post 1', 'Database connection error', '192.168.1.3', 'New York', 'Windows 10', 'Chrome', '2025-01-15 10:05:00', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36');
INSERT INTO `exception_log` VALUES ('6', '/api/comments', 'POST', 'nickname=Test&email=test@example.com&content=Test comment', 'Posting a new comment', 'Invalid email format', '192.168.1.4', 'Los Angeles', 'macOS', 'Firefox', '2025-02-20 08:35:00', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0');

-- ----------------------------
-- Table structure for friend
-- ----------------------------
DROP TABLE IF EXISTS `friend`;
CREATE TABLE `friend` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nickname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '昵称',
  `description` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '描述',
  `website` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '站点',
  `avatar` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '头像',
  `is_published` bit(1) NOT NULL COMMENT '公开或隐藏',
  `views` int NOT NULL COMMENT '点击次数',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of friend
-- ----------------------------
INSERT INTO `friend` VALUES ('1', 'Tech Friend', 'A blog focused on the latest technology news and reviews.', 'https://techfriend.com', 'https://techfriend.com/avatar.jpg', '', '2000', '2025-01-01 00:00:00');
INSERT INTO `friend` VALUES ('2', 'Travel Buddy', 'Sharing travel experiences and destination guides.', 'https://travelbuddy.com', 'https://travelbuddy.com/avatar.jpg', '', '1500', '2024-12-15 00:00:00');
INSERT INTO `friend` VALUES ('3', 'Hidden Friend', 'This is a hidden friend link.', 'https://hiddenfriend.com', 'https://hiddenfriend.com/avatar.jpg', '\0', '300', '2024-11-20 00:00:00');
INSERT INTO `friend` VALUES ('4', 'Tech Friend', 'A blog focused on the latest technology news and reviews.', 'https://techfriend.com', 'https://techfriend.com/avatar.jpg', '', '2000', '2025-01-01 00:00:00');
INSERT INTO `friend` VALUES ('5', 'Travel Buddy', 'Sharing travel experiences and destination guides.', 'https://travelbuddy.com', 'https://travelbuddy.com/avatar.jpg', '', '1500', '2024-12-15 00:00:00');
INSERT INTO `friend` VALUES ('6', 'Hidden Friend', 'This is a hidden friend link.', 'https://hiddenfriend.com', 'https://hiddenfriend.com/avatar.jpg', '\0', '300', '2024-11-20 00:00:00');
INSERT INTO `friend` VALUES ('7', 'Tech Friend', 'A blog focused on the latest technology news and reviews.', 'https://techfriend.com', 'https://techfriend.com/avatar.jpg', '', '2000', '2025-01-01 00:00:00');
INSERT INTO `friend` VALUES ('8', 'Travel Buddy', 'Sharing travel experiences and destination guides.', 'https://travelbuddy.com', 'https://travelbuddy.com/avatar.jpg', '', '1500', '2024-12-15 00:00:00');
INSERT INTO `friend` VALUES ('9', 'Hidden Friend', 'This is a hidden friend link.', 'https://hiddenfriend.com', 'https://hiddenfriend.com/avatar.jpg', '\0', '300', '2024-11-20 00:00:00');

-- ----------------------------
-- Table structure for login_log
-- ----------------------------
DROP TABLE IF EXISTS `login_log`;
CREATE TABLE `login_log` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '用户名称',
  `ip` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT 'ip',
  `ip_source` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT 'ip来源',
  `os` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '操作系统',
  `browser` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '浏览器',
  `status` bit(1) DEFAULT NULL COMMENT '登录状态',
  `description` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '操作描述',
  `create_time` datetime NOT NULL COMMENT '登录时间',
  `user_agent` varchar(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT 'user-agent用户代理',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of login_log
-- ----------------------------
INSERT INTO `login_log` VALUES ('1', 'admin', '192.168.1.5', 'New York', 'Windows 10', 'Chrome', '', 'Successful login', '2025-04-20 08:15:00', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36');
INSERT INTO `login_log` VALUES ('2', 'user1', '192.168.2.2', 'Los Angeles', 'macOS', 'Safari', '\0', 'Incorrect password', '2025-04-19 16:40:00', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15');
INSERT INTO `login_log` VALUES ('3', 'admin', '192.168.1.5', 'New York', 'Windows 10', 'Chrome', '', 'Successful login', '2025-04-20 08:15:00', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36');
INSERT INTO `login_log` VALUES ('4', 'user1', '192.168.2.2', 'Los Angeles', 'macOS', 'Safari', '\0', 'Incorrect password', '2025-04-19 16:40:00', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15');
INSERT INTO `login_log` VALUES ('5', 'admin', '192.168.1.5', 'New York', 'Windows 10', 'Chrome', '', 'Successful login', '2025-04-20 08:15:00', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36');
INSERT INTO `login_log` VALUES ('6', 'user1', '192.168.2.2', 'Los Angeles', 'macOS', 'Safari', '\0', 'Incorrect password', '2025-04-19 16:40:00', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15');

-- ----------------------------
-- Table structure for moment
-- ----------------------------
DROP TABLE IF EXISTS `moment`;
CREATE TABLE `moment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `content` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '动态内容',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `likes` int DEFAULT NULL COMMENT '点赞数量',
  `is_published` bit(1) NOT NULL COMMENT '是否公开',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of moment
-- ----------------------------
INSERT INTO `moment` VALUES ('1', '111', '2025-04-27 23:44:15', '111', '');
INSERT INTO `moment` VALUES ('2', '222', '2025-04-27 23:44:26', '224', '');

-- ----------------------------
-- Table structure for operation_log
-- ----------------------------
DROP TABLE IF EXISTS `operation_log`;
CREATE TABLE `operation_log` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '操作者用户名',
  `uri` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '请求接口',
  `method` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '请求方式',
  `param` varchar(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '请求参数',
  `description` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '操作描述',
  `ip` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT 'ip',
  `ip_source` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT 'ip来源',
  `os` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '操作系统',
  `browser` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '浏览器',
  `times` int NOT NULL COMMENT '请求耗时（毫秒）',
  `create_time` datetime NOT NULL COMMENT '操作时间',
  `user_agent` varchar(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT 'user-agent用户代理',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of operation_log
-- ----------------------------

-- ----------------------------
-- Table structure for schedule_job
-- ----------------------------
DROP TABLE IF EXISTS `schedule_job`;
CREATE TABLE `schedule_job` (
  `job_id` bigint NOT NULL AUTO_INCREMENT COMMENT '任务id',
  `bean_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT 'spring bean名称',
  `method_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '方法名',
  `params` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '参数',
  `cron` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT 'cron表达式',
  `status` tinyint DEFAULT NULL COMMENT '任务状态',
  `remark` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '备注',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`job_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of schedule_job
-- ----------------------------
INSERT INTO `schedule_job` VALUES ('1', 'redisSyncScheduleTask', 'syncBlogViewsToDatabase', '', '0 0 1 * * ?', '1', '每天凌晨一点，从Redis将博客浏览量同步到数据库', '2020-11-17 23:45:42');
INSERT INTO `schedule_job` VALUES ('2', 'visitorSyncScheduleTask', 'syncVisitInfoToDatabase', '', '0 0 0 * * ?', '1', '清空当天Redis访客标识，记录当天的PV和UV，更新当天所有访客的PV和最后访问时间，更新城市新增访客UV数', '2021-02-05 08:14:28');

-- ----------------------------
-- Table structure for schedule_job_log
-- ----------------------------
DROP TABLE IF EXISTS `schedule_job_log`;
CREATE TABLE `schedule_job_log` (
  `log_id` bigint NOT NULL AUTO_INCREMENT COMMENT '任务日志id',
  `job_id` bigint NOT NULL COMMENT '任务id',
  `bean_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT 'spring bean名称',
  `method_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '方法名',
  `params` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '参数',
  `status` tinyint NOT NULL COMMENT '任务执行结果',
  `error` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci COMMENT '异常信息',
  `times` int NOT NULL COMMENT '耗时（单位：毫秒）',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`log_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of schedule_job_log
-- ----------------------------

-- ----------------------------
-- Table structure for site_setting
-- ----------------------------
DROP TABLE IF EXISTS `site_setting`;
CREATE TABLE `site_setting` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name_en` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `name_zh` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `value` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `type` int DEFAULT NULL COMMENT '1基础设置，2页脚徽标，3资料卡，4友链信息',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of site_setting
-- ----------------------------
INSERT INTO `site_setting` VALUES ('1', 'blogName', '博客名称', 'Geralt\'s Blog', '1');
INSERT INTO `site_setting` VALUES ('2', 'webTitleSuffix', '网页标题后缀', ' - Geralt\'s Blog', '1');
INSERT INTO `site_setting` VALUES ('3', 'footerImgTitle', '页脚图片标题', '手机看本站', '1');
INSERT INTO `site_setting` VALUES ('4', 'footerImgUrl', '页脚图片路径', '/img/qr.png', '1');
INSERT INTO `site_setting` VALUES ('5', 'copyright', 'Copyright', '{\"title\":\"Copyright © 2025 - 2025\",\"siteName\":\"GERALT\'S BLOG\"}', '1');
INSERT INTO `site_setting` VALUES ('6', 'beian', 'ICP备案号', '', '1');
INSERT INTO `site_setting` VALUES ('7', 'reward', '赞赏码', '/img/reward.jpg', '1');
INSERT INTO `site_setting` VALUES ('8', 'commentAdminFlag', '博主评论标识', 'Geralt说', '1');
INSERT INTO `site_setting` VALUES ('9', 'playlistServer', '播放器平台', 'netease', '1');
INSERT INTO `site_setting` VALUES ('10', 'playlistId', '播放器歌单', '3071528549', '1');
INSERT INTO `site_setting` VALUES ('11', 'avatar', '头像', '/img/avatar.jpg', '2');
INSERT INTO `site_setting` VALUES ('12', 'name', '昵称', 'Geralt', '2');
INSERT INTO `site_setting` VALUES ('13', 'rollText', '滚动个签', 'I DID IT IN MY WAY', '2');
INSERT INTO `site_setting` VALUES ('14', 'github', 'GitHub', 'https://github.com/GeraltWu', '2');
INSERT INTO `site_setting` VALUES ('15', 'telegram', 'Telegram', '', '2');
INSERT INTO `site_setting` VALUES ('16', 'qq', 'QQ', '', '2');
INSERT INTO `site_setting` VALUES ('17', 'bilibili', 'bilibili', 'https://space.bilibili.com/350578994?spm_id_from=333.1007.0.0', '2');
INSERT INTO `site_setting` VALUES ('18', 'netease', '网易云音乐', '', '2');
INSERT INTO `site_setting` VALUES ('19', 'email', 'email', 'wuziran1223@outlook.com', '2');
INSERT INTO `site_setting` VALUES ('20', 'favorite', '自定义', '{\r\n                    \"title\": \"最喜欢的一集\",\r\n                    \"content\": \"每一集\"\r\n                }', '2');
INSERT INTO `site_setting` VALUES ('21', 'favorite', '自定义', '{\r\n                    \"title\": \"最喜欢的一集\",\r\n                    \"content\": \"每一集\"\r\n                }', '2');
INSERT INTO `site_setting` VALUES ('22', 'favorite', '自定义', '{\r\n                    \"title\": \"最喜欢的一集\",\r\n                    \"content\": \"每一集\"\r\n                }', '2');
INSERT INTO `site_setting` VALUES ('23', 'badge', '徽标', '{\"title\":\"本博客已开源于 GitHub\",\"url\":\"https://github.com/Naccl/NBlog\",\"subject\":\"NBlog\",\"value\":\"Open Source\",\"color\":\"brightgreen\"}', '3');
INSERT INTO `site_setting` VALUES ('24', 'badge', '徽标', '{\"title\":\"由fast api强力驱动\",\"url\":\"https://spring.io/projects/spring-boot/\",\"subject\":\"Powered\",\"value\":\"Spring Boot\",\"color\":\"blue\"}', '3');
INSERT INTO `site_setting` VALUES ('25', 'badge', '徽标', '{\"title\":\"Vue.js 客户端渲染\",\"url\":\"https://cn.vuejs.org/\",\"subject\":\"SPA\",\"value\":\"Vue.js\",\"color\":\"brightgreen\"}', '3');
INSERT INTO `site_setting` VALUES ('26', 'badge', '徽标', '{\"title\":\"UI 框架 Semantic-UI\",\"url\":\"https://semantic-ui.com/\",\"subject\":\"UI\",\"value\":\"Semantic-UI\",\"color\":\"semantic-ui\"}', '3');
INSERT INTO `site_setting` VALUES ('27', 'badge', '徽标', '{\"title\":\"阿里云提供服务器及域名相关服务\",\"url\":\"https://www.aliyun.com/\",\"subject\":\"VPS & DNS\",\"value\":\"Aliyun\",\"color\":\"blueviolet\"}', '3');
INSERT INTO `site_setting` VALUES ('28', 'badge', '徽标', '{\"title\":\"静态资源托管于 GitHub\",\"url\":\"https://github.com/\",\"subject\":\"OSS\",\"value\":\"GitHub\",\"color\":\"github\"}', '3');
INSERT INTO `site_setting` VALUES ('29', 'badge', '徽标', '{\"title\":\"jsDelivr 加速静态资源\",\"url\":\"https://www.jsdelivr.com/\",\"subject\":\"CDN\",\"value\":\"jsDelivr\",\"color\":\"orange\"}', '3');
INSERT INTO `site_setting` VALUES ('30', 'badge', '徽标', '{\"color\":\"lightgray\",\"subject\":\"CC\",\"title\":\"本站点采用 CC BY 4.0 国际许可协议进行许可\",\"url\":\"https://creativecommons.org/licenses/by/4.0/\",\"value\":\"BY 4.0\"}', '3');
INSERT INTO `site_setting` VALUES ('31', 'friendContent', '友链页面信息', '随机排序，不分先后。欢迎交换友链~(￣▽￣)~*\n\n* 昵称：Naccl\n* 一句话：游龙当归海，海不迎我自来也。\n* 网址：[https://naccl.top](https://naccl.top)\n* 头像URL：[https://naccl.top/img/avatar.jpg](https://naccl.top/img/avatar.jpg)\n\n仅凭个人喜好添加友链，请在收到我的回复邮件后再于贵站添加本站链接。原则上已添加的友链不会删除，如果你发现自己被移除了，恕不另行通知，只需和我一样做就好。\n\n', '4');
INSERT INTO `site_setting` VALUES ('32', 'friendCommentEnabled', '友链页面评论开关', '1', '4');

-- ----------------------------
-- Table structure for tag
-- ----------------------------
DROP TABLE IF EXISTS `tag`;
CREATE TABLE `tag` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tag_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `color` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '标签颜色(可选)',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of tag
-- ----------------------------
INSERT INTO `tag` VALUES ('1', 'tag', 'gyg');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '用户名',
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '密码',
  `nickname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '昵称',
  `avatar` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '头像地址',
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '邮箱',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `update_time` datetime NOT NULL COMMENT '更新时间',
  `role` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '角色访问权限',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'Admin', '$2a$10$4wnwMW8Z4Bn6wR4K1YlbquQunlHM/4rvudVBX8oyfx16xeVtI6i7C', 'Admin', '/img/avatar.jpg', 'admin@naccl.top', '2020-09-21 16:47:18', '2020-09-21 16:47:22', 'ROLE_admin');

-- ----------------------------
-- Table structure for visitor
-- ----------------------------
DROP TABLE IF EXISTS `visitor`;
CREATE TABLE `visitor` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `uuid` varchar(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '访客标识码',
  `ip` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT 'ip',
  `ip_source` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT 'ip来源',
  `os` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '操作系统',
  `browser` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '浏览器',
  `create_time` datetime NOT NULL COMMENT '首次访问时间',
  `last_time` datetime NOT NULL COMMENT '最后访问时间',
  `pv` int DEFAULT NULL COMMENT '访问页数统计',
  `user_agent` varchar(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT 'user-agent用户代理',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `idx_uuid` (`uuid`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of visitor
-- ----------------------------

-- ----------------------------
-- Table structure for visit_log
-- ----------------------------
DROP TABLE IF EXISTS `visit_log`;
CREATE TABLE `visit_log` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `uuid` varchar(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '访客标识码',
  `uri` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '请求接口',
  `method` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '请求方式',
  `param` varchar(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '请求参数',
  `behavior` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '访问行为',
  `content` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '访问内容',
  `remark` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '备注',
  `ip` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT 'ip',
  `ip_source` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT 'ip来源',
  `os` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '操作系统',
  `browser` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '浏览器',
  `times` int NOT NULL COMMENT '请求耗时（毫秒）',
  `create_time` datetime NOT NULL COMMENT '访问时间',
  `user_agent` varchar(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT 'user-agent用户代理',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of visit_log
-- ----------------------------

-- ----------------------------
-- Table structure for visit_record
-- ----------------------------
DROP TABLE IF EXISTS `visit_record`;
CREATE TABLE `visit_record` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `pv` int NOT NULL COMMENT '访问量',
  `uv` int NOT NULL COMMENT '独立用户',
  `date` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '日期"02-23"',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of visit_record
-- ----------------------------
