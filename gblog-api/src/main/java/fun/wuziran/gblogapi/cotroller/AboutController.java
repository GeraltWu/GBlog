package fun.wuziran.gblogapi.cotroller;

import fun.wuziran.gblogapi.annotation.VisitLogger;
import fun.wuziran.gblogapi.enums.VisitBehavior;
import fun.wuziran.gblogapi.model.vo.Result;
import fun.wuziran.gblogapi.service.AboutService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.Parameters;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @Description
 * @Author Geralt
 * @Date 2024/7/17
 */

@Tag(name = "关于我", description = "关于我相关接口")
@RestController
//解决跨域问题
@CrossOrigin()
public class AboutController {
    @Autowired
    AboutService aboutService;

    /**
     * 获取关于我页面信息
     * VisitLogger 注解用于记录访问日志 自定义的注解
     * @return Result 是自己定义的 model，里面包含了状态码和数据
     *
     */
    @Operation(summary = "获取关于我页面信息")
    @VisitLogger(VisitBehavior.ABOUT)
    @GetMapping("/about")
    public Result about() {
        return Result.ok("获取成功", aboutService.getAboutInfo());
    }
}
