package fun.wuziran.gblogapi;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import fun.wuziran.gblogapi.entity.Blog;
import fun.wuziran.gblogapi.entity.Category;
import fun.wuziran.gblogapi.entity.Tag;
import fun.wuziran.gblogapi.model.vo.BlogInfo;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.Date;

@SpringBootTest
class GblogApiApplicationTests {
    private static final ObjectMapper objectMapper = new ObjectMapper();
    @Test
    void contextLoads() {
    }

    // 有点鸡肋啊，没办法标记好类型
    @Test
    public void testBlogInfoToJson(){
        Blog blog = new Blog();
        try {
            System.out.println(objectMapper.writeValueAsString(blog));
        } catch (JsonProcessingException e) {
            e.getMessage();
        }
    }
}
