
/* 插入 blog 表示例数据 */
INSERT INTO `blog`(`title`, `first_picture`, `content`, `description`, `is_published`, `is_recommend`, `is_appreciation_enabled`, `is_comment_enabled`, `is_private`, `is_top`, `create_time`, `update_time`, `views`, `words`, `read_time`, `category_id`, `password`) VALUES
('My First Blog Post', 'https://example.com/images/blog1.jpg', 'This is the detailed content of the first blog post.', 'This post introduces the basics of starting a blog.', b'1', b'1', b'1', b'1', b'0', b'0', '2025-01-15 10:00:00', '2025-01-15 10:00:00', 500, 1000, 5, 1, NULL),
('How to Cook Pasta', 'https://example.com/images/blog2.jpg', 'Detailed steps on how to cook perfect pasta.', 'A guide for cooking enthusiasts.', b'1', b'0', b'0', b'1', b'0', b'0', '2025-02-20 08:30:00', '2025-02-20 08:30:00', 300, 800, 4, 2, NULL),
('Private Thoughts', 'https://example.com/images/private.jpg', 'This is a private post containing personal reflections.', 'Personal reflections not for public viewing.', b'0', b'0', b'0', b'0', b'1', b'0', '2025-03-05 16:45:00', '2025-03-05 16:45:00', 0, 600, 3, 3, 'secret123');

/* 插入 blog_tag 表示例数据 */
INSERT INTO `blog_tag`(`blog_id`, `tag_id`) VALUES
(1, 1),
(1, 3),
(2, 2),
(3, 4);

/* 插入 category 表示例数据 */
INSERT INTO `category`(`category_name`) VALUES
('Technology'),
('Cooking'),
('Personal');

/* 插入 city_visitor 表示例数据 */
INSERT INTO `city_visitor`(`city`, `uv`) VALUES
('New York', 1500),
('Los Angeles', 1200),
('Chicago', 800);

/* 插入 comment 表示例数据 */
INSERT INTO `comment`(`nickname`, `email`, `avatar`, `ip`, `website`, `content`, `create_time`, `is_published`, `is_admin_comment`, `page`, `is_notice`, `blog_id`, `root_comment_id`, `parent_comment_id`) VALUES
('John Doe', 'john@example.com', 'https://example.com/avatars/john.jpg', '192.168.1.1', 'https://johndoe.com', 'Great post! Really enjoyed reading it.', '2025-01-16 11:30:00', b'1', b'0', 0, b'1', 1, -1, -1),
('Admin', 'admin@example.com', 'https://example.com/avatars/admin.jpg', '192.168.1.2', 'https://adminblog.com', 'Thank you for your kind words!', '2025-01-17 09:45:00', b'1', b'1', 0, b'0', 1, 1, 1),
('Jane Smith', 'jane@example.com', 'https://example.com/avatars/jane.jpg', '192.168.2.1', NULL, 'I have a question about the cooking time.', '2025-02-21 14:20:00', b'1', b'0', 0, b'1', 2, -1, -1);

/* 插入 exception_log 表示例数据 */
INSERT INTO `exception_log`(`uri`, `method`, `param`, `description`, `error`, `ip`, `ip_source`, `os`, `browser`, `create_time`, `user_agent`) VALUES
('/api/blog/1', 'GET', '', 'Fetching blog post 1', 'Database connection error', '192.168.1.3', 'New York', 'Windows 10', 'Chrome', '2025-01-15 10:05:00', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'),
('/api/comments', 'POST', 'nickname=Test&email=test@example.com&content=Test comment', 'Posting a new comment', 'Invalid email format', '192.168.1.4', 'Los Angeles', 'macOS', 'Firefox', '2025-02-20 08:35:00', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0');

/* 插入 friend 表示例数据 */
INSERT INTO `friend`(`nickname`, `description`, `website`, `avatar`, `is_published`, `views`, `create_time`) VALUES
('Tech Friend', 'A blog focused on the latest technology news and reviews.', 'https://techfriend.com', 'https://techfriend.com/avatar.jpg', b'1', 2000, '2025-01-01 00:00:00'),
('Travel Buddy', 'Sharing travel experiences and destination guides.', 'https://travelbuddy.com', 'https://travelbuddy.com/avatar.jpg', b'1', 1500, '2024-12-15 00:00:00'),
('Hidden Friend', 'This is a hidden friend link.', 'https://hiddenfriend.com', 'https://hiddenfriend.com/avatar.jpg', b'0', 300, '2024-11-20 00:00:00');

/* 插入 login_log 表示例数据 */
INSERT INTO `login_log`(`username`, `ip`, `ip_source`, `os`, `browser`, `status`, `description`, `create_time`, `user_agent`) VALUES
('admin', '192.168.1.5', 'New York', 'Windows 10', 'Chrome', b'1', 'Successful login', '2025-04-20 08:15:00', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'),
('user1', '192.168.2.2', 'Los Angeles', 'macOS', 'Safari', b'0', 'Incorrect password', '2025-04-19 16:40:00', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15');

/* 插入 moment 表示例数据 */
INSERT INTO `moment`(`content`, `create_time`, `likes`, `is_published`) VALUES
('Just finished a great book! #Reading #BookRecommendation', '2025-04-25 20:30:00', 56, b'1'),
('Trying out a new coffee shop nearby. The latte art is amazing! 🎨☕', '2025-04-22 11:15:00', 32, b'1'),
('Working on a new project. Excited to see how it turns out! #Work #Project', '2025-04-20 09:45:00', 48, b'1');

/* 插入 operation_log 表示例数据 */
INSERT INTO `operation_log`(`username`, `uri`, `method`, `param`, `description`, `ip`, `ip_source`, `os`, `browser`, `times`, `create_time`, `user_agent`) VALUES
('admin', '/api/blog', 'POST', 'title=New Blog&content=New content&category_id=1', 'Created a new blog post', '192.168.1.5', 'New York', 'Windows 10', 'Chrome', 250, '2025-04-20 08:30:00', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'),
('admin', '/api/comments/1', 'PUT', 'is_published=1', 'Approved a comment', '192.168.1.5', 'New York', 'Windows 10', 'Chrome', 120, '2025-04-19 14:20:00', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36');

/* 插入 schedule_job 表示例数据 */
INSERT INTO `schedule_job`(`bean_name`, `method_name`, `params`, `cron`, `status`, `remark`, `create_time`) VALUES
('blogService', 'dailyStatsUpdate', '', '0 0 3 * * ?', 1, 'Daily blog statistics update', '2025-01-01 00:00:00'),
('visitorService', 'cleanupOldVisitors', '', '0 0 4 * * ?', 1, 'Cleanup visitors older than 30 days', '2025-01-05 00:00:00');

/* 插入 schedule_job_log 表示例数据 */
INSERT INTO `schedule_job_log`(`job_id`, `bean_name`, `method_name`, `params`, `status`, `error`, `times`, `create_time`) VALUES
(1, 'blogService', 'dailyStatsUpdate', '', 0, NULL, 1500, '2025-04-27 03:00:05'),
(2, 'visitorService', 'cleanupOldVisitors', '', 0, NULL, 2000, '2025-04-27 04:00:08'),
(1, 'blogService', 'dailyStatsUpdate', '', 1, 'Database connection timeout', 1800, '2025-04-26 03:00:03');

/* 插入 tag 表示例数据 */
INSERT INTO `tag`(`tag_name`, `color`) VALUES
('Technology', '#3498db'),
('Food', '#2ecc71'),
('Personal', '#e74c3c'),
('Travel', '#f39c12');

/* 插入 user 表示例数据 */
INSERT INTO `user`(`username`, `password`, `nickname`, `avatar`, `email`, `create_time`, `update_time`, `role`) VALUES
('admin', '$2a$10$EXAMPLEHASHPASSWORD1', 'Admin', 'https://example.com/avatars/admin.jpg', 'admin@example.com', '2025-01-01 00:00:00', '2025-04-20 08:15:00', 'ADMIN'),
('user1', '$2a$10$EXAMPLEHASHPASSWORD2', 'Regular User', 'https://example.com/avatars/user1.jpg', 'user1@example.com', '2025-02-10 14:30:00', '2025-02-10 14:30:00', 'USER'),
('contributor', '$2a$10$EXAMPLEHASHPASSWORD3', 'Contributor', 'https://example.com/avatars/contributor.jpg', 'contributor@example.com', '2025-03-15 09:45:00', '2025-03-15 09:45:00', 'CONTRIBUTOR');

/* 插入 visitor 表示例数据 */
INSERT INTO `visitor`(`uuid`, `ip`, `ip_source`, `os`, `browser`, `create_time`, `last_time`, `pv`, `user_agent`) VALUES
('a1b2c3d4-5678-9012-3456-7890abcdef12', '192.168.1.6', 'New York', 'Windows 10', 'Chrome', '2025-04-20 10:00:00', '2025-04-25 15:30:00', 15, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'),
('b2c3d4e5-f678-9012-3456-7890abcdef13', '192.168.2.3', 'Los Angeles', 'macOS', 'Safari', '2025-04-21 14:15:00', '2025-04-26 08:45:00', 10, 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15');

/* 插入 visit_log 表示例数据 */
INSERT INTO `visit_log`(`uuid`, `uri`, `method`, `param`, `behavior`, `content`, `remark`, `ip`, `ip_source`, `os`, `browser`, `times`, `create_time`, `user_agent`) VALUES
('a1b2c3d4-5678-9012-3456-7890abcdef12', '/blog/1', 'GET', '', 'View Blog', 'Viewed blog post 1', 'Regular visit', '192.168.1.6', 'New York', 'Windows 10', 'Chrome', 250, '2025-04-20 10:05:00', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'),
('a1b2c3d4-5678-9012-3456-7890abcdef12', '/about', 'GET', '', 'View Page', 'Viewed about page', 'Regular visit', '192.168.1.6', 'New York', 'Windows 10', 'Chrome', 180, '2025-04-20 10:10:00', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36');

/* 插入 visit_record 表示例数据 */
INSERT INTO `visit_record`(`pv`, `uv`, `date`) VALUES
(500, 150, '04-20'),
(450, 130, '04-21'),
(600, 170, '04-22'),
(550, 160, '04-23'),
(700, 190, '04-24'),
(650, 180, '04-25');