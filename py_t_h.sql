/*
 Navicat Premium Data Transfer

 Source Server         : mysql
 Source Server Type    : MySQL
 Source Server Version : 80027
 Source Host           : localhost:3306
 Source Schema         : py_t_h

 Target Server Type    : MySQL
 Target Server Version : 80027
 File Encoding         : 65001

 Date: 04/06/2022 14:40:59
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for py_t_h
-- ----------------------------
DROP TABLE IF EXISTS `py_t_h`;
CREATE TABLE `py_t_h`  (
  `id` int NOT NULL,
  `collect_time` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `temp` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `humi` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `box_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of py_t_h
-- ----------------------------
INSERT INTO `py_t_h` VALUES (0, '2022/05/19 15:39:32', '24.35', '54.55', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (1, '2022/05/19 15:39:33', '24.36', '54.52', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (2, '2022/05/19 15:39:35', '24.36', '54.49', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (3, '2022/05/19 15:39:39', '24.39', '54.49', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (4, '2022/05/19 15:39:41', '24.39', '54.49', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (5, '2022/05/19 15:39:43', '24.37', '54.42', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (6, '2022/05/19 15:39:45', '24.39', '54.43', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (7, '2022/05/19 15:39:47', '24.38', '54.43', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (8, '2022/05/19 15:39:49', '24.37', '54.42', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (9, '2022/05/19 15:39:51', '24.37', '54.42', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (10, '2022/05/19 15:39:53', '24.38', '54.43', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (11, '2022/05/19 15:39:55', '24.38', '54.39', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (12, '2022/05/19 15:39:57', '24.38', '54.39', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (13, '2022/05/19 15:39:59', '24.39', '54.36', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (14, '2022/05/19 15:40:01', '24.38', '54.33', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (15, '2022/05/19 15:40:03', '24.38', '54.3', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (16, '2022/05/19 15:40:05', '24.36', '54.3', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (17, '2022/05/19 15:40:07', '24.34', '54.3', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (18, '2022/05/19 15:40:08', '24.34', '54.3', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (19, '2022/05/19 15:40:11', '24.34', '54.33', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (20, '2022/05/19 15:40:12', '24.34', '54.36', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (21, '2022/05/19 15:40:15', '24.34', '54.42', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (22, '2022/05/19 15:40:16', '24.36', '54.42', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (23, '2022/05/19 15:40:19', '24.35', '54.48', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (24, '2022/05/19 15:40:21', '24.34', '54.51', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (25, '2022/05/19 15:40:22', '24.34', '54.55', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (26, '2022/05/19 15:40:24', '24.34', '54.58', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (27, '2022/05/19 15:40:26', '24.34', '54.61', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (28, '2022/05/19 15:40:29', '24.35', '54.58', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (29, '2022/05/19 15:40:32', '24.37', '54.58', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (30, '2022/05/19 15:40:34', '24.4', '54.55', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (31, '2022/05/19 15:40:36', '24.39', '54.52', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (32, '2022/05/19 15:40:40', '24.39', '54.46', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (33, '2022/05/19 15:40:42', '24.38', '54.46', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (34, '2022/05/19 15:40:44', '24.38', '54.46', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (35, '2022/05/19 15:40:46', '24.38', '54.46', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (36, '2022/05/19 15:40:48', '24.40', '54.44', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (37, '2022/06/02 22:08:23', '24.30', '54.42', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (38, '2022/06/02 22:11:43', '24.39', '54.45', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (39, '2022/06/02 22:14:41', '24.38', '54.42', 'W-2020-001');
INSERT INTO `py_t_h` VALUES (40, '2022/06/02 23:02:23', '24.37', '54.43', 'W-2020-001');

SET FOREIGN_KEY_CHECKS = 1;
